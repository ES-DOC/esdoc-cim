<?xml version="1.0" encoding="UTF-8"?>
<!-- really only using XSLT 2.0 for the <xsl:result-document> element -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:UML="omg.org/UML1.3"
     exclude-result-prefixes="xsl xs UML">
    
    <!-- ************ -->
    <!-- header stuff -->
    <!-- ************ -->
    
    <!-- output an XML file -->
    <xsl:output method="html" indent="yes"/>
    
    <!-- ignore free text and whitespace-->
    <xsl:template match="text()"/>
    <xsl:strip-space elements="*"/>
    
    <!-- some useful global variables  -->
    <xsl:param name="version">undefined</xsl:param>
    <xsl:param name="namespace">http://www.purl.org/org/esmetadata/cim</xsl:param>
    <xsl:param name="sort-attributes">false</xsl:param>
    <xsl:param name="debug">false</xsl:param>
    <xsl:param name="output-enumerations">true</xsl:param>
    <xsl:param name="output-codelists">true</xsl:param>

    <xsl:variable name="lowerCase">abcdefghijklmnopqrstuvwxyz</xsl:variable>
    <xsl:variable name="upperCase">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
    <xsl:variable name="newline">
        <xsl:text>       
</xsl:text>
    </xsl:variable>
    
    <!-- EA outputs XMI v1.1; so this XSL is tailored to that -->
    <!-- strange things might happen at other versions -->
    <xsl:template match="XMI[@xmi.version='1.1']">
        <xsl:if test="$version='undefined'">
            <xsl:message terminate="yes">
                <xsl:text> please specify a version parameter </xsl:text>
            </xsl:message>
        </xsl:if>
        <xsl:if test="$namespace='undefined'">
            <xsl:message terminate="yes">
                <xsl:text> please specify a CIM namespace (ie: 'http://www.purl.org/esmetadata/cim') </xsl:text>
            </xsl:message>
        </xsl:if>
        <xsl:if test="$debug='true'">
            <xsl:message>
                <xsl:value-of select="$newline"/>
            </xsl:message>
            <xsl:choose>
                <xsl:when test="$sort-attributes='true'">
                    <xsl:message>
                        <xsl:text> UML attributes will be processed in lexical order </xsl:text>
                        <xsl:value-of select="$sort-attributes"/>
                    </xsl:message>
                </xsl:when>
                <xsl:when test="not($sort-attributes='true')">
                    <xsl:message>
                        <xsl:text> UML attributes will be processed in the order in which they appear </xsl:text>
                        <xsl:value-of select="$sort-attributes"/>
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
        <xsl:variable name="fileName" select="concat('enumerations_',$version,'.html')"/>
        <xsl:result-document href="{$fileName}">
            <xsl:comment>
                <xsl:value-of select="concat(' ',$fileName,' ')"/>
            </xsl:comment>
            <xsl:comment>
                <xsl:value-of
                    select="concat(' generated: ',format-dateTime(current-dateTime(), '[D] [MNn] [Y], [H]:[m]'),' ')"
                />
            </xsl:comment>
            <xsl:value-of select="$newline"/>
            <style>
                <xsl:text>
                    table.cim_enumerations                      { border: 1px solid #000000; }
                    table.cim_enumerations tr                   { vertical-align: top; }
                    table.cim_enumerations td                   { border: 1px solid #000000; }
                    table.cim_enumerations tr.header td         { font-weight: bold; text-align: center; }
                    table.cim_enumerations tr.package_label td  { font-style: italic; background: #cccccc; }
                </xsl:text>
            </style>
            <xsl:value-of select="$newline"/>
            <xsl:apply-templates select="XMI.content/UML:Model"/>
        </xsl:result-document>
    </xsl:template>
    
    <!-- uh-oh, XMI at a different version -->
    <xsl:template match="XMI">
        <xsl:message terminate="yes">
            <xsl:text>unsupported XMI version: </xsl:text>
            <xsl:value-of select="@xmi.version"/>
        </xsl:message>
    </xsl:template>
  
    <!-- look at each package -->
    <xsl:template match="UML:Package">
        <xsl:variable name="packageName" select="@name"/>
        
        <xsl:if test="$debug='true'">
            <xsl:message>
                <xsl:value-of select="$newline"/>
            </xsl:message>
            <xsl:message>
                <xsl:text>processing package: </xsl:text>
                <xsl:value-of select="$packageName"/>
            </xsl:message>
        </xsl:if>
        
            <!-- if this is the top-level package (ie: the root of the domain model) -->
            <!-- then create the table -->
            <xsl:variable name="depth" select="count(ancestor::UML:Package)"/>
            <xsl:choose>
                <xsl:when test="$depth=0">
                    <table class='cim_enumerations'>
                        <tr class='header'>
                            <td>name</td>
                            <td>type</td>
                            <td>values</td>
                            <td>notes</td>
                        </tr>
                        <xsl:apply-templates/>
                    </table>
                </xsl:when>
                <xsl:otherwise>
                    <tr class='package_label'>
                        <td colspan="4">
                            Package: <xsl:value-of select="$packageName"/>
                        </td>
                    </tr>
                    <xsl:apply-templates/>
                </xsl:otherwise>
            </xsl:choose>
            <xsl:value-of select="$newline"/>            
    </xsl:template>
    
    
    <xsl:template match="UML:Package//UML:Class">
        <xsl:if test="$debug='true'">
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
            <xsl:when test="$classStereotype='enumeration'">
                <xsl:if test="$debug='true'">
                    <xsl:message>
                        <xsl:text> it's an enumeration </xsl:text>
                    </xsl:message>
                </xsl:if>
                <xsl:if test="$output-enumerations='true'">                
                    <xsl:call-template name="enumerationTemplate"/>
                </xsl:if>
            </xsl:when>            
            <xsl:when test="$classStereotype='codelist'">
                <xsl:if test="$debug='true'">
                    <xsl:message>
                        <xsl:text> it's a codelist </xsl:text>
                    </xsl:message>
                </xsl:if>                
                <xsl:if test="$output-codelists='true'">
                    <xsl:call-template name="codelistTemplate"/>
                </xsl:if>
            </xsl:when>
            <!--
            <xsl:when test="$classStereotype='unused'">
                <xsl:call-template name="unusedTemplate"/>
            </xsl:when>            
            <xsl:when test="$classStereotype='extensible'">
                <xsl:call-template name="extensibleTemplate"/>
            </xsl:when>            
            <xsl:when test="$classStereotype='abstract'">
                <xsl:call-template name="abstractTemplate"/>
            </xsl:when>
            <xsl:when test="$classStereotype='attribute'">                
                <xsl:call-template name="simpleTypeTemplate"/>
            </xsl:when>            
            <xsl:otherwise>
                <xsl:call-template name="complexTypeTemplate"/>
            </xsl:otherwise>
            -->
        </xsl:choose>        
    </xsl:template>    
        
    <xsl:template name="enumerationTemplate">
        <xsl:variable name="id" select="@xmi.id"/>
        <xsl:variable name="open" select="//UML:TaggedValue[@tag='open'][@modelElement=$id]/@value='true'"/>
        
        <tr class="enumeration">

            <!-- name -->
            <td>
                <xsl:value-of select="@name"/>
            </td>
        
            <!-- type -->
            <td>enumeration</td>
            
            <!-- values -->
            <td>
                <ul>
                    <xsl:for-each select="./UML:Classifier.feature/UML:Attribute">
                    <!--<xsl:for-each select=".//descendant::UML:Atribute">-->
                        <xsl:sort select="@name[$sort-attributes='true']" case-order="lower-first"/>
                        <li><xsl:value-of select="@name"/></li>
                    </xsl:for-each>
                </ul>
            </td>
        
            <!-- notes -->
            <td>
                <xsl:if test="$open">
                    open
                </xsl:if>
                <xsl:text disable-output-escaping="yes"><![CDATA[&nbsp;]]></xsl:text>
            </td>
            
        </tr>
        
    </xsl:template>
    
    <xsl:template name="codelistTemplate">
        <xsl:variable name="id" select="@xmi.id"/>
        <xsl:variable name="open" select="//UML:TaggedValue[@tag='open'][@modelElement=$id]/@value='true'"/>
        
        <tr class="codelist">
            
            <!-- name -->
            <td>
                <xsl:value-of select="@name"/>
            </td>
            
            <!-- type -->
            <td>codelist</td>
            
            <!-- values -->
            <td>
                <ul>
                    <xsl:for-each select="./UML:Classifier.feature/UML:Attribute">
                        <!--<xsl:for-each select=".//descendant::UML:Atribute">-->
                        <xsl:sort select="@name[$sort-attributes='true']" case-order="lower-first"/>
                        <li><xsl:value-of select="@name"/></li>
                    </xsl:for-each>
                </ul>
            </td>
            
            <!-- notes -->
            <td>
                <xsl:if test="$open">
                    open
                </xsl:if>
                <xsl:text disable-output-escaping="yes"><![CDATA[&nbsp;]]></xsl:text>
            </td>
        </tr>
    </xsl:template>
    
    
    
    
    <xsl:template name="lowerCaseTemplate">
        <xsl:param name="string"/>
        <!-- TODO: somewhere in this mess I am passing multiple nodes in as string -->
        <!-- the [1] gets around this -->
        <xsl:value-of select="translate($string[1],$upperCase,$lowerCase)"/>
    </xsl:template>
    
    <xsl:template name="upperCaseTemplate">
        <xsl:param name="string"/>
        <xsl:value-of select="translate($string,$lowerCase,$upperCase)"/>
    </xsl:template>
    
</xsl:stylesheet>