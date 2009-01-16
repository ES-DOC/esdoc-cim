<?xml version="1.0" encoding="UTF-8"?>
<!-- only using XSLT 2.0 for the <result-document> element -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:UML="omg.org/UML1.3"
    exclude-result-prefixes="UML">

    <!-- ************ -->
    <!-- header stuff -->
    <!-- ************ -->

    <!-- output an XML file -->
    <xsl:output method="xml" indent="yes"/>

    <!-- ignore free text and whitespace-->
    <xsl:template match="text()"/>
    <xsl:strip-space elements="*"/>

    <!-- some useful global variables  -->
    <xsl:variable name="lowerCase">abcdefghijklmnopqrstuvwxyz</xsl:variable>
    <xsl:variable name="upperCase">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
    <xsl:variable name="newline">
        <xsl:text>       
</xsl:text>
    </xsl:variable>
    <!-- set to 0 turn off printing -->
    <xsl:variable name="debug" select="0"/>

    <!-- ********************* -->
    <!-- "top-level" templates -->
    <!-- ********************* -->

    <!-- EA outputs XMI v1.1; so this XSL is tailored to that -->
    <!-- strange things might happen at other versions -->
    <xsl:template match="XMI[@xmi.version='1.1']">
        <!-- apply templates to the UML:Model -->
        <!-- and ignore  UML:Diagram, etc. -->
        <xsl:apply-templates select="XMI.content/UML:Model"/>
    </xsl:template>

    <!-- uh-oh, XMI at a different version -->
    <xsl:template match="XMI">
        <xsl:message terminate="yes">
            <xsl:text>unsupported XMI version: </xsl:text>
            <xsl:value-of select="@xmi.version"/>
        </xsl:message>
    </xsl:template>

    <!-- every package is its own schema file -->
    <!-- each package includes all other schemas -->
    <xsl:template match="UML:Package">
        <xsl:variable name="packageName" select="@name"/>
        <xsl:variable name="fileName" select="concat($packageName,'.xsd')"/>

        <xsl:if test="$debug">
            <xsl:message>
                <xsl:value-of select="$newline"/>
            </xsl:message>
            <xsl:message>
                <xsl:text>processing package: </xsl:text>
                <xsl:value-of select="$packageName"/>
            </xsl:message>
        </xsl:if>

        <xsl:result-document href="{$fileName}">
            <!-- add some useful comments about the file -->
            <xsl:comment>
                <xsl:value-of select="concat(' ',$fileName,' ')"/>
            </xsl:comment>
            <xsl:value-of select="$newline"/>
            <xsl:comment>
                <xsl:value-of
                    select="concat(' generated: ',format-date(current-date(),'[D] [MNn] [Y]'),' ')"
                />
            </xsl:comment>
            <xsl:value-of select="$newline"/>
            
            <!-- HERE IS A HACK; INCLUDING EXTERNAL NAMESPACES BY HAND -->
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                xmlns:gml="http://www.opengis.net/gml/3.2"
                xmlns:gmd="http://www.isotc211.org/2005/gmd"
                xmlns:gridspec="http://www.gfdl.noaa.gov/gridspec">
                <xsl:value-of select="$newline"/>
                <xsl:comment>
                    <xsl:text> these relative paths should really be URLs, but accessing them online cripples performance </xsl:text>
                </xsl:comment>
                <xsl:value-of select="$newline"/>                
                <xs:import namespace="http://www.opengis.net/gml/3.2"
                schemaLocation="gml/3.2.1/gml.xsd"/>
                <xs:import namespace="http://www.isotc211.org/2005/gmd"
                    schemaLocation="iso/19139/20070417/gmd/gmd.xsd"/>
                <xs:import namespace="http://www.w3.org/1999/xlink"
                    schemaLocation="xlink/1.0.0/xlinks.xsd"/>
                <!-- HERE ENDETH THE HACK -->
                
                <xsl:for-each select="//UML:Package[@name!=$packageName]">
                    <xs:include schemaLocation="{concat(@name,'.xsd')}"/>
                </xsl:for-each>
                <xsl:apply-templates/>
            </xs:schema>
        </xsl:result-document>
    </xsl:template>

    <!-- every UML class (within a package) is either a complexType or a simpleType -->
    <!-- <<document>> stereotypes are also global elements -->
    <xsl:template match="UML:Package//UML:Class">

        <xsl:variable name="classStereotype"
            select="translate(./UML:ModelElement.taggedValue/UML:TaggedValue[@tag='stereotype']/@value,$upperCase,$lowerCase)"/>

        <xsl:if test="$debug">
            <xsl:message>
                <xsl:text>processing class: </xsl:text>
                <xsl:value-of select="@name"/>
            </xsl:message>
        </xsl:if>

        <xsl:choose>
            <xsl:when test="$classStereotype='enumeration'">
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text>it's an enumeration </xsl:text>
                    </xsl:message>
                </xsl:if>
                <xsl:call-template name="enumerationTemplate"/>
            </xsl:when>
            <xsl:when test="$classStereotype='codelist'">
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text>it's a codelist </xsl:text>
                    </xsl:message>
                </xsl:if>
                <xsl:call-template name="codelistTemplate"/>
            </xsl:when>

            <!-- if it's not a simpleType (codelist or enumeration) -->
            <!-- then it must be a complexType -->
            <xsl:otherwise>
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text>it's a complexType </xsl:text>
                    </xsl:message>
                </xsl:if>

                <xsl:call-template name="complexTypeTemplate"/>
            </xsl:otherwise>
        </xsl:choose>
        
        <xsl:if test="$classStereotype='document'">
            <xsl:if test="$debug">
                <xsl:message>
                    <xsl:text>it's a document too </xsl:text>
                </xsl:message>
            </xsl:if>
            <xsl:call-template name="documentTemplate"/>
        </xsl:if>
        
    </xsl:template>

    <!-- ***************** -->
    <!-- named templates -->
    <!-- ***************** -->

    <!-- enumerations (simpleType) -->
    <xsl:template name="enumerationTemplate">
        <xs:simpleType name="{@name}">
            <xsl:apply-templates mode="UMLclass"/>
            <xs:restriction base="xs:string">
                <xsl:for-each select="descendant::UML:Attribute">
                    <xsl:sort case-order="lower-first" select="@name"/>
                    <xs:enumeration value="{@name}">
                        <xsl:apply-templates mode="UMLattribute"/>
                    </xs:enumeration>
                </xsl:for-each>
            </xs:restriction>
        </xs:simpleType>
    </xsl:template>

    <!-- codelists (simpleType) -->
    <xsl:template name="codelistTemplate">

        <xs:simpleType name="{@name}">
            <xsl:apply-templates mode="UMLclass"/>
            <!-- a codelist is a union of xs:string... -->
            <xs:union>
                <xsl:attribute name="memberTypes">
                    <xsl:value-of select="concat('xs:string ',@name,'Enumeration')"/>
                </xsl:attribute>
            </xs:union>
        </xs:simpleType>

        <xs:simpleType>
            <xsl:attribute name="name">
                <xsl:value-of select="concat(@name,'Enumeration')"/>
            </xsl:attribute>
            <!-- ...and an enumeration -->
            <xs:restriction base="xs:string">
                <xsl:for-each select="descendant::UML:Attribute">
                    <xsl:sort case-order="lower-first" select="@name"/>
                    <xs:enumeration value="{@name}">
                        <xsl:apply-templates mode="UMLattribute"/>
                    </xs:enumeration>
                </xsl:for-each>
            </xs:restriction>
        </xs:simpleType>

    </xsl:template>

    <!-- <<reference>> elements use XLinks -->
    <xsl:template name="referenceTemplate">
        <!--
        not sure about making it nillable
        <xsl:attribute name="nillable">
            <xsl:text>true</xsl:text>
        </xsl:attribute>
        -->
        <xs:complexType>
            <xs:attribute ref="xlink:href" use="required"/>
            <!-- <xs:attributeGroup ref="xlink:simpleLink"/> -->
        </xs:complexType>
    </xsl:template>

    <!-- global elements (documents) -->
    <xsl:template name="documentTemplate">
        <xsl:variable name="documentName"
            select="concat(translate(substring(@name,1,1),$upperCase,$lowerCase),substring(@name,2))"/>

        <!-- <<document>> x is just a global element of type complexType x -->
        <xs:element name="{$documentName}">
            <xsl:apply-templates mode="UMLclass"/>
            <xs:complexType>
                <xs:complexContent>
                    <xs:extension base="{@name}">
                        <!-- add document-specific elements here -->
                        <xs:sequence>
                            <xsl:for-each
                                select="//UML:Class[@name='Document']/descendant::UML:Attribute">
                                <xsl:sort case-order="lower-first" select="@name"/>
                                <xsl:variable name="attMin"
                                    select="descendant::UML:TaggedValue[@tag='lowerBound']/@value"/>
                                <xsl:variable name="attMax"
                                    select="descendant::UML:TaggedValue[@tag='upperBound']/@value"/>
                                <xsl:variable name="attType"
                                    select="descendant::UML:TaggedValue[@tag='type']/@value"/>
                                <xsl:variable name="attStereotype"
                                    select="translate(descendant::UML:TaggedValue[@tag='stereotype']/@value,$upperCase,$lowerCase)"/>
                                <xsl:if
                                    test="string($attMax)!='1' or 
                                    ( 
                                    (not($attStereotype='enumeration' or $attStereotype='codelist' or $attType='Boolean' or $attType='URI' or translate($attType,$upperCase,$lowerCase)='enumeration' or translate($attType,$upperCase,$lowerCase)='codelist'))
                                    and
                                    (not (translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='enumeration' or translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='codelist'))
                                    )">
                                    <xsl:call-template name="elementTemplate">
                                        <xsl:with-param name="min" select="$attMin"/>
                                        <xsl:with-param name="max" select="$attMax"/>
                                        <xsl:with-param name="type" select="$attType"/>
                                        <xsl:with-param name="stereotype" select="$attStereotype"/>
                                    </xsl:call-template>
                                </xsl:if>
                            </xsl:for-each>
                        </xs:sequence>
                        <!-- add document-specific attributes here -->
                        <xsl:for-each
                            select="//UML:Class[@name='Document']/descendant::UML:Attribute">
                            <xsl:sort case-order="lower-first" select="@name"/>
                            <xsl:variable name="attMin"
                                select="descendant::UML:TaggedValue[@tag='lowerBound']/@value"/>
                            <xsl:variable name="attMax"
                                select="descendant::UML:TaggedValue[@tag='upperBound']/@value"/>
                            <xsl:variable name="attType"
                                select="descendant::UML:TaggedValue[@tag='type']/@value"/>
                            <xsl:variable name="attStereotype"
                                select="translate(descendant::UML:TaggedValue[@tag='stereotype']/@value,$upperCase,$lowerCase)"/>
                            <xsl:if
                                test="string($attMax)='1' and 
                                ( 
                                ($attStereotype='enumeration' or $attStereotype='codelist' or $attType='Boolean' or $attType='URI' or translate($attType,$upperCase,$lowerCase)='enumeration' or translate($attType,$upperCase,$lowerCase)='codelist')
                                or
                                (translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='enumeration' or translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='codelist')
                                )">
                                <xsl:call-template name="attributeTemplate">
                                    <xsl:with-param name="min" select="$attMin"/>
                                    <xsl:with-param name="max" select="$attMax"/>
                                    <xsl:with-param name="type" select="$attType"/>
                                    <xsl:with-param name="stereotype" select="$attStereotype"/>
                                </xsl:call-template>
                            </xsl:if>
                        </xsl:for-each>
                    </xs:extension>
                </xs:complexContent>
            </xs:complexType>
        </xs:element>
    </xsl:template>

    <!-- local elements -->
    <xsl:template name="elementTemplate">
        <xsl:param name="min"/>
        <xsl:param name="max"/>
        <xsl:param name="type"/>
        <xsl:param name="stereotype"/>

        <xsl:element name="xs:element">
            <xsl:attribute name="name">
                <xsl:value-of select="@name"/>
            </xsl:attribute>
            <xsl:attribute name="minOccurs">
                <xsl:value-of select="$min"/>
            </xsl:attribute>
            <xsl:attribute name="maxOccurs">
                <xsl:choose>
                    <xsl:when test="string($max)='*'">
                        <xsl:text>unbounded</xsl:text>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="$max"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>

            <xsl:choose>
                <!-- the UML attribute might be an explicit <<reference>> -->
                <xsl:when test="$stereotype='reference'">
                    <xsl:call-template name="referenceTemplate"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:call-template name="typeTemplate">
                        <xsl:with-param name="type" select="$type"/>
                    </xsl:call-template>
                </xsl:otherwise>
            </xsl:choose>

            <xsl:apply-templates mode="UMLattribute"/>
        </xsl:element>

    </xsl:template>

    <!-- local attributes -->
    <xsl:template name="attributeTemplate">
        <xsl:param name="min"/>
        <xsl:param name="max"/>
        <xsl:param name="type"/>
        <xsl:param name="stereotype"/>

        <xsl:element name="xs:attribute">
            <xsl:attribute name="name">
                <xsl:value-of select="@name"/>
            </xsl:attribute>
            <xsl:attribute name="use">
                <xsl:choose>
                    <xsl:when test="$min=0">
                        <xsl:text>optional</xsl:text>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:text>required</xsl:text>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:call-template name="typeTemplate">
                <xsl:with-param name="type" select="$type"/>
            </xsl:call-template>
            <xsl:apply-templates mode="UMLattribute"/>
        </xsl:element>

    </xsl:template>

    <!-- complexTypes -->
    <xsl:template name="complexTypeTemplate">
        <xsl:variable name="class" select="."/>

        <!-- all classes (that aren't codelists or enumerations) are complexTypes -->
        <xs:complexType name="{@name}">
            <xsl:apply-templates mode="UMLclass"/>

            <!-- first check if this is a specialisation of another class -->
            <xsl:variable name="generalisation"
                select="//UML:Generalization[@subtype=$class/@xmi.id]"/>
            <xsl:if test="$generalisation">

                <xsl:variable name="generalClass"
                    select="//UML:Class[@xmi.id=$generalisation/attribute::supertype]"/>
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:value-of select="$class/@name"/>
                        <xsl:text> is a specialisation of </xsl:text>
                        <xsl:value-of select="$generalClass/@name"/>
                    </xsl:message>
                </xsl:if>
                <!-- have to do this as text b/c I don't close the tags until much later -->
                <xsl:text disable-output-escaping="yes">
                    &lt;xs:complexContent&gt;
                    &lt;xs:extension base="</xsl:text>
                <xsl:value-of select="$generalClass/attribute::name"/>
                <xsl:text disable-output-escaping="yes">"&gt;
                </xsl:text>
            </xsl:if>

            <!-- all elements must preceed any attributes, and must be grouped w/in xs:sequence -->
            <xs:sequence>

                <!-- next chack if there are any associations which have this class as an endpoint -->
                <xsl:apply-templates
                    select="//UML:Association//UML:AssociationEnd[@type=$class/@xmi.id]/ancestor::UML:Association"
                    mode="UMLclass">
                    <xsl:sort case-order="lower-first"
                        select="descendant::UML:AssociationEnd[1]/@name"/>
                    <xsl:sort case-order="lower-first"
                        select="descendant::UML:AssociationEnd[2]/@name"/>
                    <xsl:with-param name="class" select="$class"/>
                </xsl:apply-templates>

                <!-- next check if any of the (UML) attributes should be (XML) elements -->
                <xsl:for-each select="descendant::UML:Attribute">
                    <xsl:sort case-order="lower-first" select="@name"/>

                    <!-- A UML attribute is an XML element, unless it is of type x-->
                    <!-- where x is an enumeration, codelist, or (certain) built-in type. -->
                    <!-- Otherwise it is an XML attribute, -->
                    <!-- unless it has an upperBound > 1 -->

                    <xsl:variable name="attMin"
                        select="descendant::UML:TaggedValue[@tag='lowerBound']/@value"/>
                    <xsl:variable name="attMax"
                        select="descendant::UML:TaggedValue[@tag='upperBound']/@value"/>
                    <xsl:variable name="attType"
                        select="descendant::UML:TaggedValue[@tag='type']/@value"/>
                    <xsl:variable name="attStereotype"
                        select="translate(descendant::UML:TaggedValue[@tag='stereotype']/@value,$upperCase,$lowerCase)"/>

                    <xsl:if test="$debug">
                        <xsl:message>
                            <xsl:text>processing attribute: </xsl:text>
                            <xsl:value-of select="@name"/>
                        </xsl:message>
                        <xsl:message>
                            <xsl:text>min: </xsl:text>
                            <xsl:value-of select="$attMin"/>
                        </xsl:message>
                        <xsl:message>
                            <xsl:text>max: </xsl:text>
                            <xsl:value-of select="$attMax"/>
                        </xsl:message>
                        <xsl:message>
                            <xsl:text>type: </xsl:text>
                            <xsl:value-of select="$attType"/>
                        </xsl:message>
                        <xsl:message>
                            <xsl:text>stereotype: </xsl:text>
                            <xsl:value-of select="$attStereotype"/>
                        </xsl:message>
                        <xsl:message>
                            <xsl:text>stereotype of type class: </xsl:text>
                            <xsl:copy-of
                                select="//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name"
                            />
                        </xsl:message>
                    </xsl:if>
                    <!-- if the upperBound is greater than one -->
                    <!-- or it is not an explicit enumeration or codelist or boolean -->
                    <!-- or it is not a type which is itself an explicit enumeration or codelist -->
                    <!-- (have to test $attMax as a string, b/c it might equal "*") -->
                    <xsl:choose>

                        <xsl:when
                            test="string($attMax)!='1' or 
                            ( 
                            (not($attStereotype='enumeration' or $attStereotype='codelist' or $attType='Boolean' or $attType='URI' or translate($attType,$upperCase,$lowerCase)='enumeration' or translate($attType,$upperCase,$lowerCase)='codelist'))
                            and
                            (not (translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='enumeration' or translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='codelist'))
                            )">

                            <xsl:if test="$debug">
                                <xsl:message>
                                    <xsl:text>it's an element </xsl:text>
                                </xsl:message>
                            </xsl:if>
                            <!-- then it must be an XML element -->
                            <xsl:call-template name="elementTemplate">
                                <xsl:with-param name="min" select="$attMin"/>
                                <xsl:with-param name="max" select="$attMax"/>
                                <xsl:with-param name="type" select="$attType"/>
                                <xsl:with-param name="stereotype" select="$attStereotype"/>
                            </xsl:call-template>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:if test="$debug">
                                <xsl:message>
                                    <xsl:text>it's an attribute (deal w/ it later) </xsl:text>
                                </xsl:message>
                            </xsl:if>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:for-each>

            </xs:sequence>
            <!-- that's if for the elements, now we loop again and process any attributes -->

            <xsl:for-each select="descendant::UML:Attribute">
                <xsl:sort case-order="lower-first" select="@name"/>

                <xsl:variable name="attMin"
                    select="descendant::UML:TaggedValue[@tag='lowerBound']/@value"/>
                <xsl:variable name="attMax"
                    select="descendant::UML:TaggedValue[@tag='upperBound']/@value"/>
                <xsl:variable name="attType"
                    select="descendant::UML:TaggedValue[@tag='type']/@value"/>
                <xsl:variable name="attStereotype"
                    select="translate(descendant::UML:TaggedValue[@tag='stereotype']/@value,$upperCase,$lowerCase)"/>

                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text>processing attribute: </xsl:text>
                        <xsl:value-of select="@name"/>
                    </xsl:message>
                    <xsl:message>
                        <xsl:text>min: </xsl:text>
                        <xsl:value-of select="$attMin"/>
                    </xsl:message>
                    <xsl:message>
                        <xsl:text>max: </xsl:text>
                        <xsl:value-of select="$attMax"/>
                    </xsl:message>
                    <xsl:message>
                        <xsl:text>type: </xsl:text>
                        <xsl:value-of select="$attType"/>
                    </xsl:message>
                    <xsl:message>
                        <xsl:text>stereotype: </xsl:text>
                        <xsl:value-of select="$attStereotype"/>
                    </xsl:message>
                    <xsl:message>
                        <xsl:text>stereotype of type class: </xsl:text>
                        <xsl:copy-of
                            select="//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name"
                        />
                    </xsl:message>
                </xsl:if>

                <!-- this should be the inverse of the above test -->
                <xsl:choose>

                    <xsl:when
                        test="string($attMax)='1' and 
                        ( 
                        ($attStereotype='enumeration' or $attStereotype='codelist' or $attType='Boolean' or $attType='URI' or translate($attType,$upperCase,$lowerCase)='enumeration' or translate($attType,$upperCase,$lowerCase)='codelist')
                        or
                        (translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='enumeration' or translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='codelist')
                        )">

                        <xsl:if test="$debug">
                            <xsl:message>
                                <xsl:text>it's an attribute </xsl:text>
                            </xsl:message>
                        </xsl:if>

                        <xsl:call-template name="attributeTemplate">
                            <xsl:with-param name="min" select="$attMin"/>
                            <xsl:with-param name="max" select="$attMax"/>
                            <xsl:with-param name="type" select="$attType"/>
                            <xsl:with-param name="stereotype" select="$attStereotype"/>
                        </xsl:call-template>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:if test="$debug">
                            <xsl:message>
                                <xsl:text>it's an element (already dealt w/ it) </xsl:text>
                            </xsl:message>
                        </xsl:if>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>

            <!-- don't forget to close any tags from a generalisation -->
            <xsl:if test="$generalisation">
                <xsl:text disable-output-escaping="yes">  
                    &lt;/xs:extension&gt;
                    &lt;/xs:complexContent&gt;
                </xsl:text>
            </xsl:if>

        </xs:complexType>

    </xsl:template>

    <!-- ****************** -->
    <!-- "helper" templates -->
    <!-- ****************** -->

    <!-- most of these templates use the "mode" attribute -->
    <!-- to prevent them from matching in unwanted situations -->

    <!-- copy appropriate documentation over -->
    <xsl:template match="UML:Class//UML:TaggedValue[@tag='documentation']" mode="UMLclass">
        <xsl:call-template name="commentTemplate"/>
    </xsl:template>
    <xsl:template match="UML:Attribute//UML:TaggedValue[@tag='description']" mode="UMLattribute">
        <xsl:call-template name="commentTemplate"/>
    </xsl:template>
    <xsl:template name="commentTemplate">
        <xsl:if test="string-length(normalize-space(@value))>1">
            <xsl:element name="xs:annotation">
                <xsl:element name="xs:documentation">
                    <!-- documentation might have embedded entities; don't escape these -->
                    <xsl:value-of select="@value" disable-output-escaping="yes"/>
                </xsl:element>
            </xsl:element>
        </xsl:if>
    </xsl:template>

    <!-- an association from one (UML) class to another -->
    <xsl:template match="UML:Association" mode="UMLclass">
        <xsl:param name="class"/>

        <!-- I am matching the associationEnd that is _not_ the current class -->
        <!-- b/c UML associations are "backwards" -->

        <xsl:for-each select="descendant::UML:AssociationEnd">

            <xsl:if
                test="(following-sibling::UML:AssociationEnd/@type=$class/@xmi.id) or (preceding-sibling::UML:AssociationEnd/@type=$class/@xmi.id)">
                <xsl:variable name="endType" select="@type"/>
                <xsl:variable name="endClass" select="//UML:Class[@xmi.id=$endType]"/>

                <!-- don't bother recording the element if it has a min & max of 0 -->
                <xsl:if test="@multiplicity!='0'">

                    <xsl:element name="xs:element">


                        <!-- work out its name -->
                        <xsl:attribute name="name">
                            <xsl:choose>
                                <!-- if the associationEnd has a role, use that as the name -->
                                <xsl:when test="@name">
                                    <xsl:value-of select="@name"/>
                                </xsl:when>
                                <xsl:otherwise>
                                    <!-- otherwise, use a camelCase version of the class name -->
                                    <xsl:variable name="name"
                                        select="//UML:Class[@xmi.id=$endType]/@name"/>
                                    <xsl:value-of
                                        select="concat(translate(substring($name,1,1),$upperCase,$lowerCase),substring($name,2))"
                                    />
                                </xsl:otherwise>
                            </xsl:choose>
                        </xsl:attribute>

                        <!-- and the max/min  -->
                        <xsl:choose>
                            <xsl:when test="@multiplicity='*'">
                                <xsl:attribute name="minOccurs">1</xsl:attribute>
                                <xsl:attribute name="maxOccurs">unbounded</xsl:attribute>
                            </xsl:when>
                            <!--
                            <xsl:when test="@multiplicity='0'">
                                <xsl:attribute name="minOccurs">0</xsl:attribute>
                                <xsl:attribute name="maxOccurs">0</xsl:attribute>
                            </xsl:when>
                            -->
                            <xsl:when test="@multiplicity='0..*'">
                                <xsl:attribute name="minOccurs">0</xsl:attribute>
                                <xsl:attribute name="maxOccurs">unbounded</xsl:attribute>
                            </xsl:when>
                            <xsl:when test="@multiplicity='0..1'">
                                <xsl:attribute name="minOccurs">0</xsl:attribute>
                                <xsl:attribute name="maxOccurs">1</xsl:attribute>
                            </xsl:when>
                            <xsl:when test="@multiplicity='1'">
                                <xsl:attribute name="minOccurs">1</xsl:attribute>
                                <xsl:attribute name="maxOccurs">1</xsl:attribute>
                            </xsl:when>
                            <xsl:when test="@multiplicity='1..'">
                                <xsl:attribute name="minOccurs">1</xsl:attribute>
                                <xsl:attribute name="maxOccurs">unbounded</xsl:attribute>
                            </xsl:when>
                            <xsl:when test="@multiplicity='1..*'">
                                <xsl:attribute name="minOccurs">1</xsl:attribute>
                                <xsl:attribute name="maxOccurs">unbounded</xsl:attribute>
                            </xsl:when>
                            <xsl:otherwise>
                                <!-- multiplicity is not specified; assume 1..1 -->
                                <xsl:attribute name="minOccurs">1</xsl:attribute>
                                <xsl:attribute name="maxOccurs">1</xsl:attribute>
                            </xsl:otherwise>
                        </xsl:choose>

                        <!-- and its type -->

                        <xsl:choose>
                            <!-- if the endClass is a <<document>> -->
                            <!-- or if the association is an explicit <<reference>> -->
                            <!-- and the association is not an explicit <<inline>> -->
                            <xsl:when
                                test="
                            (translate($endClass/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='document')
                            or
                            ( (translate(./descendant::UML:TaggedValue[@tag='destStereotype']/@value,$upperCase,$lowerCase)='reference') or (translate(./descendant::UML:TaggedValue[@tag='sourceStereotype']/@value,$upperCase,$lowerCase)='reference') )
                            and not
                            ( (translate(./descendant::UML:TaggedValue[@tag='destStereotype']/@value,$upperCase,$lowerCase)='inline') or (translate(./descendant::UML:TaggedValue[@tag='sourceStereotype']/@value,$upperCase,$lowerCase)='inline') )                            
                            ">
                                <!-- then use XLinks -->
                                <!-- (specify the class as a reference) -->
                                <xsl:call-template name="referenceTemplate"/>
                            </xsl:when>
                            <!--  otherwise use its native type -->
                            <!-- (specify the class inline) -->
                            <xsl:otherwise>
                                <xsl:attribute name="type">
                                    <xsl:value-of select="$endClass/@name"/>
                                </xsl:attribute>
                            </xsl:otherwise>
                        </xsl:choose>

                    </xsl:element>

                </xsl:if>

            </xsl:if>
        </xsl:for-each>

    </xsl:template>

    <!-- convert UML named types to XML named types -->
    <xsl:template name="typeTemplate">
        <xsl:param name="type"/>
        <xsl:if test="$type">
            <xsl:choose>
                <xsl:when
                    test="translate($type,$upperCase,$lowerCase)='characterstring' or
                    translate($type,$upperCase,$lowerCase)='string' or
                    translate($type,$upperCase,$lowerCase)='char'">
                    <!-- some external packages use String & Char for types -->
                    <!-- bad, bad external packages -->
                    <xsl:attribute name="type">
                        <xsl:text>xs:string</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="translate($type,$upperCase,$lowerCase)='integer' or
                    translate($type,$upperCase,$lowerCase)='int'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:integer</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="translate($type,$upperCase,$lowerCase)='real'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:double</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="translate($type,$upperCase,$lowerCase)='boolean'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:boolean</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="translate($type,$upperCase,$lowerCase)='uri'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:anyURI</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when
                    test="translate($type,$upperCase,$lowerCase)='date' or
                    translate($type,$upperCase,$lowerCase)='datetime'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:dateTime</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:attribute name="type">
                        <xsl:value-of select="$type"/>
                    </xsl:attribute>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:if>
    </xsl:template>

</xsl:stylesheet>
