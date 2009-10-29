<?xml version="1.0" encoding="UTF-8"?>
<!-- really only using XSLT 2.0 for the <xsl:result-document> element -->
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
    <xsl:param name="version">undefined</xsl:param>
    <xsl:param name="sort-attributes" select="false()"/>
    <xsl:param name="debug" select="false()"/>

    <xsl:variable name="lowerCase">abcdefghijklmnopqrstuvwxyz</xsl:variable>
    <xsl:variable name="upperCase">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
    <xsl:variable name="newline">
        <xsl:text>       
</xsl:text>
    </xsl:variable>

    <!-- ********************* -->
    <!-- "top-level" templates -->
    <!-- ********************* -->

    <!-- EA outputs XMI v1.1; so this XSL is tailored to that -->
    <!-- strange things might happen at other versions -->
    <xsl:template match="XMI[@xmi.version='1.1']">
        <xsl:if test="$version='undefined'">
            <xsl:message terminate="yes">
                <xsl:text> please specify a version parameter </xsl:text>
            </xsl:message>
        </xsl:if>
        <xsl:if test="$debug">
            <xsl:message>
                <xsl:value-of select="$newline"/>
            </xsl:message>
            <xsl:choose>
                <xsl:when test="$sort-attributes">
                    <xsl:message>
                        <xsl:text> UML attributes will be processed in lexical order </xsl:text>
                    </xsl:message>
                </xsl:when>
                <xsl:when test="not($sort-attributes)">
                    <xsl:message>
                        <xsl:text> UML attributes will be processed in the order in which they appear </xsl:text>
                    </xsl:message>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:message terminate="yes">
                        <xsl:text> invalid sorting order specified </xsl:text>
                    </xsl:message>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:if>

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
                    select="concat(' generated: ',format-dateTime(current-dateTime(), '[D] [MNn] [Y], [H]:[m]'),' ')"
                />
            </xsl:comment>
            <xsl:value-of select="$newline"/>

            <!-- HERE IS A HACK; INCLUDING EXTERNAL NAMESPACES BY HAND -->
            <!-- not sure why I can't use XPath for "xmlns" attribute -->
            <!-- but specifying the following as icky <xsl:text> gets around that problem  -->
            <xsl:text disable-output-escaping="yes">&lt;xs:schema
             elementFormDefault="qualified" attributeFormDefault="unqualified"
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns:xlink="http://www.w3.org/1999/xlink"
             xmlns:gml="http://www.opengis.net/gml/3.2"
             xmlns:gmd="http://www.isotc211.org/2005/gmd"
            </xsl:text>
            <xsl:text disable-output-escaping="yes">xmlns="http://www.metaforclimate.eu/cim/</xsl:text>
            <xsl:value-of select="$version"/>
            <xsl:text disable-output-escaping="yes">" 
            targetNamespace="http://www.metaforclimate.eu/cim/</xsl:text>
            <xsl:value-of select="$version"/>
            <xsl:text disable-output-escaping="yes">"&gt;</xsl:text>

            <!--                
            <xs:schema                 
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                xmlns:gml="http://www.opengis.net/gml/3.2"
                xmlns:gmd="http://www.isotc211.org/2005/gmd"
                xmlns="{concat('http://www.metaforclimate.eu/cim/',$version)}"
                targetNamespace="{concat('http://www.metaforclimate.eu/cim/',$version)}"
                elementFormDefault="qualified" attributeFormDefault="unqualified">
            -->
            <xsl:value-of select="$newline"/>
            <xsl:comment>
                <xsl:text> these relative paths could really be URLs, but accessing them online cripples performance </xsl:text>
            </xsl:comment>
            <xsl:value-of select="$newline"/>
            <xs:import namespace="http://www.w3.org/1999/xlink"
                schemaLocation="../external_schemas/xlink/1.0.0/xlinks.xsd"/>
            <xs:import namespace="http://www.opengis.net/gml/3.2"
                schemaLocation="../external_schemas/gml/3.2.1/gml.xsd"/>
            <xs:import namespace="http://www.isotc211.org/2005/gmd"
                schemaLocation="../external_schemas/iso/19139/20070417/gmd/gmd.xsd"/>
            <!-- HERE ENDETH THE HACK -->

            <xsl:for-each select="//UML:Package[@name!=$packageName]">
                <xsl:if test="./ancestor::UML:Package">
                    <!-- include every package that is _not_ the "parent" package -->
                    <xs:include schemaLocation="{concat(@name,'.xsd')}"/>
                </xsl:if>
            </xsl:for-each>

            <!-- if this is the top-level package (ie: the root of the domain model) -->
            <!-- then create a root element "CIMRecord"-->
            <!-- which can contain a reference to _any_ <<document>> -->
            <!-- (this enables the CIM to work with GeoNetworks) -->
            <xsl:variable name="depth" select="count(ancestor::UML:Package)"/>
            <xsl:if test="$depth=0">
                <xsl:comment>
                    <xsl:text> a CIMRecord can include any (single) &lt;&lt;document&gt;&gt; </xsl:text>
                </xsl:comment>
                <xsl:value-of select="$newline"/>
                <xs:element name="CIMRecord">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="id" minOccurs="1" maxOccurs="1" type="Identifier">
                                <xs:annotation>
                                    <xs:documentation>a unique indentifier for this
                                        document</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:choice minOccurs="1" maxOccurs="1">
                                <xsl:for-each select="//UML:Stereotype[@name='document']">
                                    <xsl:variable name="documentName">
                                        <xsl:call-template name="camelCaseTemplate">
                                            <xsl:with-param name="string"
                                                select="./ancestor::UML:ModelElement.stereotype/ancestor::UML:Class/@name"
                                            />
                                        </xsl:call-template>
                                    </xsl:variable>
                                    <xs:element ref="{$documentName}"/>
                                </xsl:for-each>
                            </xs:choice>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xsl:if>
            <!-- carry on with the parsing... -->
            <xsl:apply-templates/>

            <xsl:value-of select="$newline"/>
            <xsl:text disable-output-escaping="yes">&lt;/xs:schema&gt;</xsl:text>
            <!--            
            </xs:schema>
            -->

        </xsl:result-document>
    </xsl:template>

    <!-- every UML class (within a package) is either a complexType or a simpleType -->
    <!-- <<document>> stereotypes are also global elements -->
    <xsl:template match="UML:Package//UML:Class">

        <xsl:if test="$debug">
            <xsl:message>
                <xsl:text>processing class: </xsl:text>
                <xsl:value-of select="@name"/>
            </xsl:message>
        </xsl:if>

        <xsl:variable name="classStereotype">
            <xsl:call-template name="lowerCaseTemplate">
                <xsl:with-param name="string"
                    select="./UML:ModelElement.taggedValue/UML:TaggedValue[@tag='stereotype']/@value"
                />
            </xsl:call-template>
        </xsl:variable>

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

            <!--
            don't need to do anything special for _global_ <<abstract>> classes;
            there's nothing different about them - only when other classes point to them do I need to bother
            <xsl:when test="$classStereotype='abstract'">
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text>it's abstract </xsl:text>
                    </xsl:message>
                </xsl:if>
                <xsl:call-template name="abstractTemplate"/>
            </xsl:when>
            -->

            <!-- simpleTypes are used in order to force UML classes to be used as XML attributes -->
            <!-- This mixes a bit of implementation-specific logic into the UML; but I can live with that -->
            <xsl:when test="$classStereotype='attribute'">
                <xsl:if test="$debug">
                    <xsl:message>
                        <xsl:text> it's a simpleType </xsl:text>
                    </xsl:message>
                </xsl:if>
                <xsl:call-template name="simpleTypeTemplate"/>
            </xsl:when>

            <!-- if it's not a simpleType (codelist or enumeration or explicit attribute) -->
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
                    <xsl:text> it's a document too </xsl:text>
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

    <!-- enumerations -->
    <xsl:template name="enumerationTemplate">
        <!-- is this enumeration part of a codelist? -->
        <xsl:param name="codelist" select="false()"/>
        <!-- if so, is it "open" or "closed?" -->
        <xsl:param name="open" select="false()"/>

        <xsl:variable name="name">
            <xsl:choose>
                <!-- this might be part of a codelist -->
                <xsl:when test="$codelist">
                    <xsl:value-of select="concat(@name,'_Enumeration')"/>
                </xsl:when>
                <!-- or it might be a standard enumeration -->
                <xsl:otherwise>
                    <xsl:value-of select="@name"/>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:variable>

        <xs:simpleType name="{$name}">
            <xs:restriction base="xs:string">

                <xsl:for-each select="descendant::UML:Attribute">
                    <!-- this cunning little bit of XSL below will find @name only if $sort-attribute='true' -->
                    <!-- therefore, the xsl:sort element does nothing when $sort-attribute='false' -->
                    <!-- this is used throughout this stylesheet -->
                    <xsl:sort select="@name[$sort-attributes]" case-order="lower-first"/>

                    <xs:enumeration value="{@name}">
                        <xsl:apply-templates mode="UMLattribute"/>
                    </xs:enumeration>
                </xsl:for-each>
                <xsl:if test="$open">
                    <xs:enumeration value="other"/>
                </xsl:if>
            </xs:restriction>
        </xs:simpleType>
    </xsl:template>


    <!-- codelist template -->
    <xsl:template name="codelistTemplate">
        <xsl:variable name="id" select="@xmi.id"/>
        <!-- assume codelists are "closed" unless they are specified "open" -->
        <xsl:variable name="open"
            select="//UML:TaggedValue[@tag='open'][@modelElement=$id]/@value='true'"/>

        <xs:complexType name="{@name}" mixed="{$open}">
            <xsl:apply-templates mode="UMLclass"/>
            <xs:attribute name="value" type="{concat(@name,'_Enumeration')}" use="required"/>
        </xs:complexType>
        <xsl:call-template name="enumerationTemplate">
            <xsl:with-param name="open" select="$open"/>
            <xsl:with-param name="codelist" select="true()"/>
        </xsl:call-template>
    </xsl:template>

    <xsl:template name="referenceTemplate">
        <xsl:param name="class"/>
        <xsl:param name="attribute"/>
        <xsl:param name="association"/>
        <!-- actually $association is an associationEnd -->

        <!-- isAttribute is true if the reference stereotype is being used on a UML Attribute -->
        <!-- isAssociation is true if the reference stereotype is being used on a UML Association -->
        <xsl:variable name="isAttribute" select="empty($association)"/>
        <xsl:variable name="isAssociation" select="empty($attribute)"/>

        <!-- all references are implemented as choices between... -->
        <xs:complexType>
            <xs:choice>
                <!-- ...the reference type as defined in the CIM... -->
                <xs:element name="reference">
                    <xs:complexType>
                        <xs:sequence>
                            <xsl:for-each
                                select="//UML:Class[@name='Reference']/descendant::UML:Attribute">
                                <xsl:sort case-order="lower-first" select="@name[$sort-attributes]"/>
                                <xsl:call-template name="element-attributeTemplate">
                                    <xsl:with-param name="element" select="true()"/>
                                    <xsl:with-param name="attribute" select="false()"/>
                                </xsl:call-template>
                            </xsl:for-each>
                        </xs:sequence>
                        <xsl:for-each
                            select="//UML:Class[@name='Reference']/descendant::UML:Attribute">
                            <xsl:sort case-order="lower-first" select="@name[$sort-attributes]"/>
                            <xsl:call-template name="element-attributeTemplate">
                                <xsl:with-param name="element" select="false()"/>
                                <xsl:with-param name="attribute" select="true()"/>
                            </xsl:call-template>
                        </xsl:for-each>
                        <!-- ...with one extra hard-coded attribute... -->
                        <xs:attribute ref="xlink:href" use="optional"/>
                    </xs:complexType>
                </xs:element>

                <xsl:variable name="classStereotype">
                    <xsl:call-template name="lowerCaseTemplate">
                        <xsl:with-param name="string"
                            select="$class//UML:TaggedValue[@tag='stereotype']/@value"/>
                    </xsl:call-template>
                </xsl:variable>

                <!-- ...or the locally embedded referenced type... -->
                <xsl:choose>
                    <!-- if it's a reference to a Document, then I need to hard-code some bits... -->
                    <xsl:when test=".//UML:TaggedValue[@tag='type']/@value='Document'">
                        <xsl:element name="xs:element">
                            <xsl:attribute name="name">
                                <xsl:call-template name="camelCaseTemplate">
                                    <xsl:with-param name="string" select="$class/@name"/>
                                </xsl:call-template>                                
                            </xsl:attribute>

                            <xs:complexType>
                                <xs:choice minOccurs="1" maxOccurs="1">
                                    <xsl:for-each select="//UML:Stereotype[@name='document']">
                                        <xsl:variable name="documentName">
                                            <xsl:call-template name="camelCaseTemplate">
                                                <xsl:with-param name="string"
                                                    select="./ancestor::UML:ModelElement.stereotype/ancestor::UML:Class/@name"
                                                />
                                            </xsl:call-template>
                                        </xsl:variable>
                                        <xs:element ref="{$documentName}"/>
                                    </xsl:for-each>
                                </xs:choice>
                            </xs:complexType>


                        </xsl:element>
                            
                            <!-- I AM HERE I AM HERE -->                        
                            
                    </xsl:when>
                    <!-- ...that type might be abstract -->
                    <xsl:when test="$classStereotype='abstract'">
                        <xsl:call-template name="abstractTemplate">
                            <xsl:with-param name="class" select="$class"/>
                            <xsl:with-param name="association" select="$association"/>
                            <xsl:with-param name="attribute" select="$attribute"/>
                        </xsl:call-template>
                    </xsl:when>
                    <!-- ...or it might be based on some external (to the domain model) class... -->
                    <xsl:when test="empty($class)">
                        <!-- if $class is empty, then I can assume the type is external (ie: the class was never found in the domain model) -->
                        <!-- if the external class is abstract then I don't know what to do... I've reached the limit of XSL cleverness -->
                        <xs:element name="{./@name}" type="{.//UML:TaggedValue[@tag='type']/@value}"
                        />
                    </xsl:when>
                    <!-- ...or it might be mercifully straightforward... -->
                    <xsl:otherwise>
                        <xsl:variable name="className">
                            <xsl:call-template name="camelCaseTemplate">
                                <xsl:with-param name="string" select="$class/@name"/>
                            </xsl:call-template>
                        </xsl:variable>                            
                        <xs:element name="{$className}" type="{$class/@name}"/>                                                    
                    </xsl:otherwise>
                </xsl:choose>

            </xs:choice>
        </xs:complexType>
    </xsl:template>

    <!-- abstract classes -->
    <xsl:template name="abstractTemplate">
        <!-- the abstract class being used -->
        <xsl:param name="class"/>
        <xsl:param name="attribute"/>
        <xsl:param name="association"/>

        <!-- isAttribute is true if the reference stereotype is being used on a UML Attribute -->
        <!-- isAssociation is true if the reference stereotype is being used on a UML Association -->
        <xsl:variable name="isAttribute" select="boolean($attribute)"/>
        <xsl:variable name="isAssociation" select="boolean($association)"/>

        <xsl:comment>
            <xsl:text> this is an abstract class </xsl:text>
        </xsl:comment>

        <xsl:element name="xs:element">
            <xsl:if test="$isAssociation">
                <xsl:variable name="name">
                    <xsl:variable name="roleName" select="$association/@name"/>
                    <xsl:variable name="className" select="$class/@name"/>
                    <xsl:choose>
                        <xsl:when test="$roleName">
                            <xsl:value-of select="$roleName"/>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:call-template name="camelCaseTemplate">
                                <xsl:with-param name="string" select="$className"/>
                            </xsl:call-template>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:variable>
                <xsl:variable name="min">
                    <xsl:call-template name="multiplicityTemplate">
                        <xsl:with-param name="multiplicity" select="@multiplicity"/>
                        <xsl:with-param name="min" select="true()"/>
                    </xsl:call-template>
                </xsl:variable>
                <xsl:variable name="max">
                    <xsl:call-template name="multiplicityTemplate">
                        <xsl:with-param name="multiplicity" select="@multiplicity"/>
                        <xsl:with-param name="max" select="true()"/>
                    </xsl:call-template>
                </xsl:variable>

                <xsl:attribute name="name" select="$name"/>
                <xsl:attribute name="minOccurs" select="$min"/>
                <xsl:attribute name="maxOccurs" select="$max"/>
            </xsl:if>

            <xsl:if test="$isAttribute">
                <xsl:attribute name="name" select="$attribute/@name"/>
                <xsl:attribute name="minOccurs"
                    select="$attribute/descendant::UML:TaggedValue[@tag='lowerBound']/@value"/>
                <xsl:attribute name="maxOccurs">
                    <xsl:variable name="max"
                        select="$attribute/descendant::UML:TaggedValue[@tag='upperBound']/@value"/>
                    <xsl:choose>
                        <xsl:when test="string($max)='*'">
                            <xsl:text>unbounded</xsl:text>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:value-of select="$max"/>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:attribute>
            </xsl:if>

            <xs:complexType>
                <xs:choice minOccurs="1" maxOccurs="1">

                    <!-- present a choice of each specialisation of the abstract class -->
                    <xsl:for-each select="//UML:Generalization[@supertype=$class/@xmi.id]">

                        <xsl:variable name="specialisedID" select="@subtype"/>
                        <xsl:variable name="specialisedClass"
                            select="//UML:Class[@xmi.id=$specialisedID]"/>
                        <!-- so long as the specialised class is not <<unused>> -->
                        <xsl:variable name="ea_xref_property">
                            <xsl:text>$ea_xref_property</xsl:text>
                        </xsl:variable>
                        <xsl:if
                            test="not(contains($specialisedClass/UML:ModelElement.taggedValue/UML:TaggedValue[@tag='$ea_xref_property']/@value,'Name=unused'))">
                            <xsl:element name="xs:element">
                                <xsl:variable name="specialisedClassName"
                                    select="$specialisedClass/@name"/>
                                <xsl:attribute name="name">
                                    <xsl:call-template name="camelCaseTemplate">
                                        <xsl:with-param name="string" select="$specialisedClassName"
                                        />
                                    </xsl:call-template>
                                </xsl:attribute>
                                <xsl:attribute name="type">
                                    <xsl:value-of select="$specialisedClassName"/>
                                </xsl:attribute>

                            </xsl:element>
                        </xsl:if>
                    </xsl:for-each>
                </xs:choice>
            </xs:complexType>

        </xsl:element>
    </xsl:template>

    <!-- global elements (documents) -->
    <xsl:template name="documentTemplate">

        <xsl:variable name="documentName">
            <xsl:call-template name="camelCaseTemplate">
                <xsl:with-param name="string" select="@name"/>
            </xsl:call-template>
        </xsl:variable>

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
                                <xsl:sort case-order="lower-first" select="@name[$sort-attributes]"/>

                                <xsl:call-template name="element-attributeTemplate">
                                    <xsl:with-param name="element" select="true()"/>
                                    <xsl:with-param name="attribute" select="false()"/>
                                </xsl:call-template>

                            </xsl:for-each>
                        </xs:sequence>

                        <!-- add document-specific attributes here -->
                        <xsl:for-each
                            select="//UML:Class[@name='Document']/descendant::UML:Attribute">
                            <xsl:sort case-order="lower-first" select="@name[$sort-attributes]"/>

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
            <!-- if the datatype is abstract, then -->
            <xsl:when
                test="//UML:Class[@name=$type]/descendant::UML:TaggedValue[@tag='stereotype']/@value='abstract' and $stereotype!='reference'">
                <!-- I am assuming that this abstract class will have been defined globally elsewhere -->
                <!-- this is just for local abstract classes -->
                <xsl:call-template name="abstractTemplate">
                    <xsl:with-param name="class" select="//UML:Class[@name=$type]"/>
                    <xsl:with-param name="attribute" select="."/>
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
                            <xsl:variable name="referencedClassName"
                                select=".//UML:TaggedValue[@tag='type']/@value"/>
                            <xsl:call-template name="referenceTemplate">

                                <xsl:with-param name="class"
                                    select="//UML:Class[@name=$referencedClassName]"/>
                                <xsl:with-param name="attribute" select="."/>
                            </xsl:call-template>
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
        <xsl:variable name="stereotype">
            <xsl:call-template name="lowerCaseTemplate">
                <xsl:with-param name="string"
                    select="./UML:ModelElement.taggedValue/UML:TaggedValue[@tag='stereotype']/@value"
                />
            </xsl:call-template>
        </xsl:variable>

        <!-- all classes (that aren't codelists or enumerations) are complexTypes -->
        <xsl:element name="xs:complexType">
            <xsl:attribute name="name" select="@name"/>
            <xsl:if test="$stereotype='abstract'">
                <xsl:attribute name="abstract">true</xsl:attribute>
            </xsl:if>

            <!-- if a class has no associations or attributes -->
            <!-- nor are there any generalisations nor specialisations of it -->
            <!-- then mixed=true (because I don't know what the heck you intend to do with it) -->
            <!-- BEWARE: HERE BE BRITTLE LOGIC -->
            <xsl:variable name="nAssociations"
                select="count(//UML:Association//UML:AssociationEnd[@type=$class/@xmi.id]/ancestor::UML:Association)"/>
            <xsl:variable name="nAttributes" select="count(descendant::UML:Attribute)"/>
            <xsl:variable name="generalisedClass"
                select="//UML:Class[@xmi.id=//UML:Generalization[@subtype=$class/@xmi.id]/@supertype]"/>
            <xsl:variable name="specialisedClass"
                select="//UML:Class[@xmi.id=//UML:Generalization[@supertype=$class/@xmi.id]/@subtype]"/>
            <xsl:variable name="nGeneralisedAssociations"
                select="count(//UML:Association//UML:AssociationEnd[@type=$generalisedClass/@xmi.id]/ancestor::UML:Association)"/>
            <xsl:variable name="nSpecialisedAssociations"
                select="count(//UML:Association//UML:AssociationEnd[@type=$specialisedClass/@xmi.id]/ancestor::UML:Association)"/>
            <xsl:variable name="nGeneralisedAttributes"
                select="count($generalisedClass/descendant::UML:Attribute)"/>
            <xsl:variable name="nSpecialisedAttributes"
                select="count($specialisedClass/descendant::UML:Attribute)"/>
            <xsl:if
                test="($nAssociations+$nAttributes+$nGeneralisedAssociations+$nGeneralisedAttributes+$nSpecialisedAssociations+$nSpecialisedAttributes)=0">
                <xsl:attribute name="mixed">true</xsl:attribute>
            </xsl:if>

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

                    <!-- first check if there are any associations which have this class as an endpoint -->
                    <!-- (associations are automatically elements) -->
                    <xsl:apply-templates
                        select="//UML:Association//UML:AssociationEnd[@type=$class/@xmi.id]/ancestor::UML:Association"
                        mode="UMLclass">
                        <xsl:sort case-order="lower-first"
                            select="descendant::UML:AssociationEnd[1]/@name[$sort-attributes]"/>
                        <xsl:sort case-order="lower-first"
                            select="descendant::UML:AssociationEnd[2]/@name[$sort-attributes]"/>
                        <xsl:with-param name="class" select="$class"/>
                    </xsl:apply-templates>

                    <!-- next check if any of the (UML) attributes should be (XML) elements -->
                    <xsl:for-each select="descendant::UML:Attribute">
                        <xsl:sort case-order="lower-first" select="@name[$sort-attributes]"/>
                        <xsl:call-template name="element-attributeTemplate">
                            <xsl:with-param name="element" select="true()"/>
                            <xsl:with-param name="attribute" select="false()"/>
                        </xsl:call-template>
                    </xsl:for-each>

                </xs:sequence>
            </xsl:if>

            <!-- that's if for the elements, now we loop again and process any attributes -->
            <xsl:for-each select="descendant::UML:Attribute">
                <xsl:sort case-order="lower-first" select="@name[$sort-attributes]"/>

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

        </xsl:element>

    </xsl:template>

    <!-- ****************** -->
    <!-- "helper" templates -->
    <!-- ****************** -->

    <!-- I'm using these 3 templates as functions -->
    <!-- which isn't very XSLT or efficient -->
    <!-- but it makes the code easier to read -->
    <xsl:template name="lowerCaseTemplate">
        <xsl:param name="string"/>
        <!-- TODO: somewhere in this mess I am passing multiple nodes in as string -->
        <!-- the [1] gets around this; but I need to fix the source of the problem -->
        <xsl:value-of select="translate($string[1],$upperCase,$lowerCase)"/>
    </xsl:template>

    <xsl:template name="upperCaseTemplate">
        <xsl:param name="string"/>
        <xsl:value-of select="translate($string,$lowerCase,$upperCase)"/>
    </xsl:template>

    <xsl:template name="camelCaseTemplate">
        <!-- just makes the 1st character lowercase; doesn't guarantee the rest is camelCase -->
        <xsl:param name="string"/>
        <xsl:variable name="start" select="translate(substring($string,1,1),$upperCase,$lowerCase)"/>
        <xsl:variable name="end" select="substring($string,2)"/>
        <xsl:value-of select="concat($start,$end)"/>
    </xsl:template>

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
                <!-- just a temporary variable to make subsequent XPath expressions simpler: -->
                <xsl:variable name="endClassId" select="@type"/>
                <!-- the class this association points to: -->
                <xsl:variable name="endClass" select="//UML:Class[@xmi.id=$endClassId]"/>
                <!-- the stereotype of that class: -->
                <xsl:variable name="endClassStereotype">
                    <xsl:call-template name="lowerCaseTemplate">
                        <xsl:with-param name="string"
                            select="$endClass/UML:ModelElement.taggedValue/UML:TaggedValue[@tag='stereotype']/@value"
                        />
                    </xsl:call-template>
                </xsl:variable>
                <!-- the stereotype of the _association_ -->
                <xsl:variable name="endStereotype">
                    <xsl:choose>
                        <xsl:when test="./descendant::UML:TaggedValue[@tag='destStereotype']">
                            <xsl:call-template name="lowerCaseTemplate">
                                <xsl:with-param name="string"
                                    select="./descendant::UML:TaggedValue[@tag='destStereotype']/@value"
                                />
                            </xsl:call-template>
                        </xsl:when>
                        <xsl:when test="./descendant::UML:TaggedValue[@tag='sourceStereotype']">
                            <xsl:call-template name="lowerCaseTemplate">
                                <xsl:with-param name="string"
                                    select="./descendant::UML:TaggedValue[@tag='sourceStereotype']/@value"
                                />
                            </xsl:call-template>
                        </xsl:when>
                    </xsl:choose>
                </xsl:variable>

                <!-- don't bother recording the element if it has a min & max of 0 -->
                <xsl:if test="@multiplicity!='0'">

                    <xsl:variable name="associationName">
                        <xsl:choose>
                            <!-- if the associationEnd has a role, use that as the name -->
                            <xsl:when test="@name">
                                <xsl:value-of select="@name"/>
                            </xsl:when>
                            <xsl:otherwise>
                                <!-- otherwise, use a camelCase version of the class name -->
                                <xsl:call-template name="camelCaseTemplate">
                                    <xsl:with-param name="string"
                                        select="//UML:Class[@xmi.id=$endClassId]/@name"/>
                                </xsl:call-template>
                            </xsl:otherwise>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:variable name="associationMin">
                        <xsl:call-template name="multiplicityTemplate">
                            <xsl:with-param name="multiplicity" select="@multiplicity"/>
                            <xsl:with-param name="min" select="true()"/>
                        </xsl:call-template>
                    </xsl:variable>
                    <xsl:variable name="associationMax">
                        <xsl:call-template name="multiplicityTemplate">
                            <xsl:with-param name="multiplicity" select="@multiplicity"/>
                            <xsl:with-param name="max" select="true()"/>
                        </xsl:call-template>
                    </xsl:variable>

                    <!-- 
                    either the association is to a normal class
                    or an abstract class
                    or a document
                    and either the association is a reference 
                    or inline
                    -->

                    <xsl:choose>
                        <!-- if the association is an explicit reference, -->
                        <!-- or the associated class is a document (and the association is not an explicit inline) -->
                        <!-- then create a reference -->
                        <xsl:when
                            test="($endClassStereotype='document' and $endStereotype!='inline') or ($endStereotype='reference')">
                            <xs:element name="{$associationName}" minOccurs="{$associationMin}"
                                maxOccurs="{$associationMax}">
                                <xsl:call-template name="referenceTemplate">
                                    <xsl:with-param name="class" select="$endClass"/>
                                    <xsl:with-param name="association" select="."/>
                                </xsl:call-template>
                            </xs:element>
                        </xsl:when>
                        <!-- if the associated class is abstract -->
                        <!-- be sure to replace the element w/ a choice of specialisations -->
                        <xsl:when test="$endClassStereotype='abstract'">
                            <xsl:call-template name="abstractTemplate">
                                <xsl:with-param name="class" select="$endClass"/>
                                <xsl:with-param name="association" select="."/>
                            </xsl:call-template>
                        </xsl:when>
                        <!-- otherwise it's just a normal element -->
                        <xsl:otherwise>
                            <xsl:element name="xs:element">
                                <xsl:attribute name="name" select="$associationName"/>
                                <xsl:attribute name="minOccurs" select="$associationMin"/>
                                <xsl:attribute name="maxOccurs" select="$associationMax"/>
                                <xsl:attribute name="type">
                                    <xsl:value-of select="$endClass/@name"/>
                                </xsl:attribute>
                            </xsl:element>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:if>
            </xsl:if>
        </xsl:for-each>

    </xsl:template>

    <xsl:template name="multiplicityTemplate">
        <xsl:param name="multiplicity"/>
        <xsl:param name="min" select="false()"/>
        <xsl:param name="max" select="false()"/>

        <xsl:choose>
            <!-- if $multiplicity is not specified, assume a min/max of 1 -->
            <xsl:when test="not(boolean($multiplicity))">
                <xsl:text>1</xsl:text>
            </xsl:when>

            <!-- if a range is specified, split $multiplicity at '..' and return the left or right string as appropriate -->
            <xsl:when test="contains($multiplicity,'..')">
                <xsl:if test="boolean($min)">
                    <xsl:variable name="left" select="substring-before($multiplicity,'..')"/>
                    <xsl:choose>
                        <xsl:when test="string($left)='*'">
                            <xsl:text>unbounded</xsl:text>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:value-of select="$left"/>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:if>
                <xsl:if test="boolean($max)">
                    <xsl:variable name="right" select="substring-after($multiplicity,'..')"/>
                    <xsl:choose>
                        <xsl:when test="string($right)='*'">
                            <xsl:text>unbounded</xsl:text>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:value-of select="$right"/>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:if>
            </xsl:when>

            <!-- otherwise, just return the single value -->
            <xsl:otherwise>
                <xsl:choose>
                    <xsl:when test="string($multiplicity)='*'">
                        <!-- with the caveat that "*" really means "0..*" -->
                        <xsl:if test="$min">
                            <xsl:text>0</xsl:text>
                        </xsl:if>
                        <xsl:if test="$max">
                            <xsl:text>unbounded</xsl:text>
                        </xsl:if>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="$multiplicity"/>
                    </xsl:otherwise>
                </xsl:choose>

            </xsl:otherwise>
        </xsl:choose>

    </xsl:template>

    <!-- convert UML named types to XML named types -->
    <xsl:template name="typeTemplate">
        <xsl:param name="type"/>

        <xsl:if test="$type">

            <xsl:variable name="lowerCaseType">
                <xsl:call-template name="lowerCaseTemplate">
                    <xsl:with-param name="string" select="$type"/>
                </xsl:call-template>
            </xsl:variable>

            <xsl:attribute name="type">
                <xsl:choose>
                    <xsl:when
                        test="$lowerCaseType='characterstring' or $lowerCaseType='string' or $lowerCaseType='char'">
                        <!-- some external packages use String & Char for types -->
                        <!-- bad, bad external packages -->
                        <xsl:text>xs:string</xsl:text>
                    </xsl:when>
                    <xsl:when test="$lowerCaseType='integer' or $lowerCaseType='int'">
                        <xsl:text>xs:integer</xsl:text>
                    </xsl:when>
                    <xsl:when test="$lowerCaseType='real' or $lowerCaseType='double'">
                        <xsl:text>xs:double</xsl:text>
                    </xsl:when>
                    <xsl:when test="$lowerCaseType='boolean'">
                        <xsl:text>xs:boolean</xsl:text>
                    </xsl:when>
                    <xsl:when test="$lowerCaseType='uri'">
                        <xsl:text>xs:anyURI</xsl:text>
                    </xsl:when>
                    <xsl:when test="$lowerCaseType='date' or $lowerCaseType='datetime'">
                        <xsl:text>xs:dateTime</xsl:text>
                    </xsl:when>
                    <!-- if it's none of those built-in types, then don't convert it to any specific XML types -->
                    <xsl:otherwise>
                        <xsl:value-of select="$type"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
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
            ($attStereotype='enumeration' or $attStereotype='Xcodelist' or $attStereotype='attribute' or translate($attType,$upperCase,$lowerCase)='enumeration' or translate($attType,$upperCase,$lowerCase)='codelist' or translate($attType,$upperCase,$lowerCase)='boolean' or translate($attType,$upperCase,$lowerCase)='uri')
            or
            (translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='enumeration' or translate(//UML:Class[@name=$attType]/UML:ModelElement.stereotype/UML:Stereotype/@name,$upperCase,$lowerCase)='xcodelist')
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
