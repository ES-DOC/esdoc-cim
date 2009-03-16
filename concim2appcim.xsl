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
    <xsl:variable name="version">0.2</xsl:variable>
    <xsl:variable name="lowerCase">abcdefghijklmnopqrstuvwxyz</xsl:variable>
    <xsl:variable name="upperCase">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
    <xsl:variable name="newline">
        <xsl:text>       
</xsl:text>
    </xsl:variable>
    <!-- set to 1 turn on printing -->
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
<<<<<<< .working
            <!--  not sure why I can't use XPath for "xmlns" attribute -->
            <xs:schema                               
                xmlns="http://www.metaforclimate.eu/cim/0.2"                
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
=======
            <!--  not sure why I can't use XPath for "xmlns" attribute -->
            <xs:schema xmlns="http://www.metaforclimate.eu/cim/0.2"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
>>>>>>> .merge-right.r382
                xmlns:xlink="http://www.w3.org/1999/xlink"
                xmlns:gml="http://www.opengis.net/gml/3.2"
                xmlns:gmd="http://www.isotc211.org/2005/gmd"
<<<<<<< .working
                targetNamespace="{concat('http://www.metaforclimate.eu/cim/',$version)}">

=======
                targetNamespace="{concat('http://www.metaforclimate.eu/cim/',$version)}"
                elementFormDefault="qualified" attributeFormDefault="unqualified">

>>>>>>> .merge-right.r382
                <xsl:value-of select="$newline"/>
                <xsl:comment>
                    <xsl:text> these relative paths could really be URLs, but accessing them online cripples performance </xsl:text>
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
<<<<<<< .working

                <!-- if this is the top-level package (ie: the root of the domain model) -->
                <!-- then create a root element "CIMRecord"-->
                <!-- which can contain a reference to _any_ <<document>> -->
                <xsl:variable name="depth" select="count(ancestor::UML:Package)"/>
                <xsl:if test="$depth=0">
                    <xsl:comment>
                        <xsl:text> a CIMRecord can include any (single) &lt;&lt;document&gt;&gt; </xsl:text>
                    </xsl:comment>
                    <xsl:value-of select="$newline"/>
                    <xs:element name="CIMRecord">
                        <xs:complexType>
                            <xs:choice>
                                <xsl:for-each select="//UML:Stereotype[@name='document']">
                                    <xsl:variable name="className"
                                        select="./ancestor::UML:ModelElement.stereotype/ancestor::UML:Class/@name"/>
                                    <xsl:variable name="documentName"
                                        select="concat(translate(substring($className,1,1),$upperCase,$lowerCase),substring($className,2))"/>
                                    <xs:element ref="{$documentName}"/>
                                </xsl:for-each>
                            </xs:choice>
                        </xs:complexType>
                    </xs:element>
                </xsl:if>
                <!-- carry on with the parsing... -->
=======

                <!-- if this is the top-level package (ie: the root of the domain model) -->
                <!-- then create a root element "CIMRecord"-->
                <!-- which can contain a reference to _any_ <<document>> -->
                <xsl:variable name="depth" select="count(ancestor::UML:Package)"/>
                <xsl:if test="$depth=0">
                    <xsl:comment>
                        <xsl:text> a CIMRecord can include any (single) &lt;&lt;document&gt;&gt; </xsl:text>
                    </xsl:comment>
                    <xsl:value-of select="$newline"/>
                    <xs:element name="CIMRecord">
                        <xs:complexType>
                            <xs:sequence>
                                <xs:element name="id" minOccurs="1" maxOccurs="1"
                                    type="Identifier">
                                    <xs:annotation>
                                        <xs:documentation>a unique indentifier for this document</xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:choice>
                                    <xsl:for-each select="//UML:Stereotype[@name='document']">
                                        <xsl:variable name="className"
                                            select="./ancestor::UML:ModelElement.stereotype/ancestor::UML:Class/@name"/>
                                        <xsl:variable name="documentName"
                                            select="concat(translate(substring($className,1,1),$upperCase,$lowerCase),substring($className,2))"/>
                                        <xs:element ref="{$documentName}"/>
                                    </xsl:for-each>
                                </xs:choice>
                            </xs:sequence>
                        </xs:complexType>
                    </xs:element>
                </xsl:if>
                <!-- carry on with the parsing... -->
>>>>>>> .merge-right.r382
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
            <xsl:when test="$classStereotype='unused'">
                <xsl:call-template name="unusedTemplate">
                    <xsl:with-param name="className" select="@name"/>
                </xsl:call-template>
            </xsl:when>
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
            <!-- simpleTypes are used in order to force UML classes to be used as XML attributes -->
            <xsl:when test="$classStereotype='attribute'">
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text> it's a simpleType</xsl:text>
                    </xsl:message>
                </xsl:if>
                <xsl:call-template name="simpleTypeTemplate"/>
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

    <!-- unused classes -->
    <xsl:template name="unusedTemplate">
        <xsl:param name="className"/>
        <xsl:comment>
            <xsl:value-of select="$className"/>
            <xsl:text> is not used </xsl:text>
        </xsl:comment>
        <xsl:value-of select="$newline"/>
    </xsl:template>

    <!-- enumerations (simpleType) -->
    <xsl:template name="enumerationTemplate">
        <xsl:param name="local" select="false()"/>

        <xsl:text disable-output-escaping="yes">
            &lt;xs:simpleType name="</xsl:text>
        <xsl:choose>
            <!-- this might be part of a codelist (a locally defined enumeration) -->
            <xsl:when test="$local">
                <xsl:value-of select="concat(@name,'_Enumeration')"/>
            </xsl:when>
            <!-- or it might be a normal (globally defined) enumeration -->
            <xsl:otherwise>
                <xsl:value-of select="@name"/>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text disable-output-escaping="yes">"&gt;
        </xsl:text>

        <xs:restriction base="xs:string">
            <xsl:for-each select="descendant::UML:Attribute">
                <xsl:sort case-order="lower-first" select="@name"/>
                <xs:enumeration value="{@name}">
                    <xsl:apply-templates mode="UMLattribute"/>
                </xs:enumeration>
            </xsl:for-each>
        </xs:restriction>

        <xsl:text disable-output-escaping="yes">
            &lt;/xs:simpleType&gt;
        </xsl:text>

    </xsl:template>

    <!-- codelists (simpleType) -->
    <xsl:template name="codelistTemplate">

        <xs:simpleType name="{@name}">
            <xsl:apply-templates mode="UMLclass"/>
            <!-- a codelist is a union of xs:string... -->
            <xs:union>
                <xsl:attribute name="memberTypes">
                    <xsl:value-of select="concat('xs:string ',@name,'_Enumeration')"/>
                </xsl:attribute>
            </xs:union>
        </xs:simpleType>
        <!-- ...and an enumeration -->
        <xsl:call-template name="enumerationTemplate">
            <xsl:with-param name="local" select="true()"/>
        </xsl:call-template>
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

                                <xsl:call-template name="element-attributeTemplate">
                                    <xsl:with-param name="element" select="true()"/>
                                    <xsl:with-param name="attribute" select="false()"/>
                                </xsl:call-template>

                            </xsl:for-each>
                        </xs:sequence>

                        <!-- add document-specific attributes here -->
                        <xsl:for-each
                            select="//UML:Class[@name='Document']/descendant::UML:Attribute">
                            <xsl:sort case-order="lower-first" select="@name"/>

                            <xsl:call-template name="element-attributeTemplate">
                                <xsl:with-param name="element" select="false()"/>
                                <xsl:with-param name="attribute" select="true()"/>
                            </xsl:call-template>

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

        <xsl:choose>
            <xsl:when test="$stereotype='unused'">
                <xsl:call-template name="unusedTemplate">
                    <xsl:with-param name="className" select="@name"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>

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
                            <!-- annotations have to come _before_ complexContent -->
                            <xsl:apply-templates mode="UMLattribute"/>
                            <xsl:call-template name="referenceTemplate"/>
                        </xsl:when>
                        <!-- otherwise, use its specified type -->
                        <xsl:otherwise>
                            <xsl:call-template name="typeTemplate">
                                <xsl:with-param name="type" select="$type"/>
                            </xsl:call-template>
                            <!-- but they can come _after_ normal elements -->
                            <xsl:apply-templates mode="UMLattribute"/>
                        </xsl:otherwise>
                    </xsl:choose>

                </xsl:element>

            </xsl:otherwise>
        </xsl:choose>

    </xsl:template>

    <!-- local attributes -->
    <xsl:template name="attributeTemplate">
        <xsl:param name="min"/>
        <xsl:param name="max"/>
        <xsl:param name="type"/>
        <xsl:param name="stereotype"/>

        <xsl:choose>
            <xsl:when test="$stereotype='unused'">
                <xsl:call-template name="unusedTemplate">
                    <xsl:with-param name="className" select="@name"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>

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
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- simpleTypes -->
    <xsl:template name="simpleTypeTemplate">

        <xsl:variable name="externalGeneralisation"
            select="./UML:ModelElement.taggedValue/UML:TaggedValue[@tag='genlinks'][1]"/>
        <xsl:variable name="generalClass"
            select="substring-before(substring-after($externalGeneralisation/attribute::value,'Parent='),';')"/>

        <xsl:if test="not(starts-with($generalClass,'xs:'))">
            <xsl:message terminate="yes">
                <xsl:value-of select="@name"/>
                <xsl:text> cannot be a simpleType because it is based on: </xsl:text>
                <xsl:value-of select="$generalClass"/>
            </xsl:message>
        </xsl:if>

        <xs:simpleType name="{@name}">
            <xs:restriction base="{$generalClass}">
                <xsl:apply-templates mode="UMLclass"/>
                <!-- not sure how to extend a simpleType via UML -->
                <!-- luckily, this hasn't come up in the CIM -->
            </xs:restriction>
        </xs:simpleType>
    </xsl:template>

    <!-- complexTypes -->
    <xsl:template name="complexTypeTemplate">
        <xsl:variable name="class" select="."/>

        <!-- all classes (that aren't codelists or enumerations) are complexTypes -->
        <xs:complexType name="{@name}">
            <xsl:apply-templates mode="UMLclass"/>

            <!-- first check if this is a specialisation of another class -->
            <xsl:variable name="internalGeneralisation"
                select="//UML:Generalization[@subtype=$class/@xmi.id]"/>
            <xsl:variable name="externalGeneralisation"
                select="./UML:ModelElement.taggedValue/UML:TaggedValue[@tag='genlinks'][1]"/>
            <xsl:variable name="simpleGeneralisation"
                select="starts-with($externalGeneralisation/attribute::value,'Parent=xs:')"/>

            <xsl:choose>
                <!-- it might be a specialisation of some other class in the domain model -->
                <xsl:when test="$internalGeneralisation">

                    <xsl:variable name="generalClass"
                        select="//UML:Class[@xmi.id=$internalGeneralisation/attribute::supertype]"/>

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
                </xsl:when>

                <xsl:otherwise>

                    <!-- or it might be a specialisation of some class outside of the domain model -->
                    <xsl:if test="$externalGeneralisation">

                        <xsl:variable name="generalClass"
                            select="substring-before(substring-after($externalGeneralisation/attribute::value,'Parent='),';')"/>

                        <xsl:if test="$debug">
                            <xsl:message>
                                <xsl:value-of select="$class/@name"/>
                                <xsl:text> is a specialisation of </xsl:text>
                                <xsl:value-of select="$generalClass"/>
                            </xsl:message>
                        </xsl:if>

                        <xsl:choose>
                            <!-- and that other class might be a simpleType -->
                            <xsl:when test="$simpleGeneralisation">
                                <xsl:text disable-output-escaping="yes">
                                &lt;xs:simpleContent&gt;
                                &lt;xs:extension base="</xsl:text>
                                <xsl:value-of select="$generalClass"/>
                                <xsl:text disable-output-escaping="yes">"&gt;
                            </xsl:text>
                            </xsl:when>
                            <!-- or not -->
                            <xsl:otherwise>
                                <xsl:text disable-output-escaping="yes">
                                &lt;xs:complexContent&gt;
                                &lt;xs:extension base="</xsl:text>
                                <xsl:value-of select="$generalClass"/>
                                <xsl:text disable-output-escaping="yes">"&gt;
                            </xsl:text>
                            </xsl:otherwise>
                        </xsl:choose>

                    </xsl:if>

                </xsl:otherwise>
            </xsl:choose>

            <!-- all elements must preceed any attributes, and must be grouped w/in xs:sequence -->
            <!-- note that simpleTypes cannot have elements -->
            <xsl:if test="not($simpleGeneralisation)">
                <xs:sequence>

                    <!-- first chack if there are any associations which have this class as an endpoint -->
                    <!-- (associations are automatically elements) -->
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

                        <xsl:call-template name="element-attributeTemplate">
                            <xsl:with-param name="element" select="true()"/>
                            <xsl:with-param name="attribute" select="false()"/>
                        </xsl:call-template>
                    </xsl:for-each>

                </xs:sequence>
            </xsl:if>

            <!-- that's if for the elements, now we loop again and process any attributes -->
            <xsl:for-each select="descendant::UML:Attribute">
                <xsl:sort case-order="lower-first" select="@name"/>

                <xsl:call-template name="element-attributeTemplate">
                    <xsl:with-param name="element" select="false()"/>
                    <xsl:with-param name="attribute" select="true()"/>
                </xsl:call-template>
            </xsl:for-each>

            <!-- don't forget to close any tags from a generalisation -->
            <xsl:if test="$internalGeneralisation or $externalGeneralisation">
                <xsl:choose>
                    <xsl:when test="$simpleGeneralisation">
                        <xsl:text disable-output-escaping="yes">  
                            &lt;/xs:extension&gt;
                            &lt;/xs:simpleContent&gt;
                        </xsl:text>

                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:text disable-output-escaping="yes">  
                            &lt;/xs:extension&gt;
                            &lt;/xs:complexContent&gt;
                        </xsl:text>

                    </xsl:otherwise>
                </xsl:choose>

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
                                <xsl:attribute name="minOccurs">0</xsl:attribute>
                                <xsl:attribute name="maxOccurs">unbounded</xsl:attribute>
                            </xsl:when>
                            <xsl:when test="@multiplicity='0'">
                                <xsl:attribute name="minOccurs">0</xsl:attribute>
                                <xsl:attribute name="maxOccurs">0</xsl:attribute>
                            </xsl:when>
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
        <xsl:variable name="lowerCaseType" select="translate($type,$upperCase,$lowerCase)"/>
        <xsl:if test="$type">
            <xsl:choose>
                <xsl:when
                    test="$lowerCaseType='characterstring' or $lowerCaseType='string' or $lowerCaseType='char'">
                    <!-- some external packages use String & Char for types -->
                    <!-- bad, bad external packages -->
                    <xsl:attribute name="type">
                        <xsl:text>xs:string</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="$lowerCaseType='integer' or $lowerCaseType='int'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:integer</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="$lowerCaseType='real' or $lowerCaseType='double'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:double</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="$lowerCaseType='boolean'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:boolean</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="$lowerCaseType='uri'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:anyURI</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <xsl:when test="$lowerCaseType='date' or $lowerCaseType='datetime'">
                    <xsl:attribute name="type">
                        <xsl:text>xs:dateTime</xsl:text>
                    </xsl:attribute>
                </xsl:when>
                <!-- if it's none of those built-in types, then don't convert it to any specific XML types -->
                <xsl:otherwise>
                    <xsl:attribute name="type">
                        <xsl:value-of select="$type"/>
                    </xsl:attribute>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:if>
    </xsl:template>

    <!-- template returns either a local element or attribute -->
    <!-- based on some rather convoluted logic -->
    <xsl:template name="element-attributeTemplate">
        <xsl:param name="element"/>
        <xsl:param name="attribute"/>

        <xsl:variable name="attMin" select="descendant::UML:TaggedValue[@tag='lowerBound']/@value"/>
        <xsl:variable name="attMax" select="descendant::UML:TaggedValue[@tag='upperBound']/@value"/>
        <xsl:variable name="attType" select="descendant::UML:TaggedValue[@tag='type']/@value"/>
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
        </xsl:if>

        <!-- isAttribute is true when... -->
        <!-- the maximum is not greater than 1 -->
        <!-- AND the stereotype is either an enumeration or codelist or explicit attribute or the type is an explicit enumeration or codelist or boolean or URI  -->
        <!-- OR the type has a stereotype of enumeration or codelist -->
        <xsl:variable name="isAttribute"
            select="string($attMax)='1' 
            and
            (
            ($attStereotype='enumeration' or $attStereotype='codelist' or $attStereotype='attribute' or translate($attType,$upperCase,$lowerCase)='enumeration' or translate($attType,$upperCase,$lowerCase)='codelist' or translate($attType,$upperCase,$lowerCase)='boolean' or translate($attType,$upperCase,$lowerCase)='uri')
            or
            (translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='enumeration' or translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='codelist')
            )"/>

        <xsl:choose>
            <!-- when isAttribute is true and you're looking for an attribute, call the attributeTemplate -->
            <xsl:when test="$isAttribute and $attribute">
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
            <xsl:when test="$isAttribute and $element">
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text>it's an attribute (deal w/ it later)</xsl:text>
                    </xsl:message>
                </xsl:if>
            </xsl:when>
            <!-- when isAttribute is false and you're looking for an element, call the elementTemplate -->
            <xsl:when test="not($isAttribute) and $element">
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text>it's an element </xsl:text>
                    </xsl:message>
                </xsl:if>
                <xsl:call-template name="elementTemplate">
                    <xsl:with-param name="min" select="$attMin"/>
                    <xsl:with-param name="max" select="$attMax"/>
                    <xsl:with-param name="type" select="$attType"/>
                    <xsl:with-param name="stereotype" select="$attStereotype"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:when test="not($isAttribute) and $attribute">
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text>it's an element (already dealt w/ it) </xsl:text>
                    </xsl:message>
                </xsl:if>
            </xsl:when>
        </xsl:choose>
    </xsl:template>


</xsl:stylesheet>
