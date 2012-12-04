This file contains information about how to view and manipulate the Common Information Model (CIM) Conceptual UML Schema (CONCIM) and Application XML Schema (APPCIM).  

In order to view and manipulate the CONCIM, a UML editor such as Enterprise Architect is required.  In order to view and manipulate the APPCIM, an XML editor such as Oxygen is recommended.  XML can be viewed as plain text, but it is not recommended for a model as complex as the CIM.  In order to translate from the CONCIM to the APPCIM (which only active CIM developers should have to do), an XSLT processor such as libXSLT is required.

This file is located at the root directory of an archived CIM version.  CIM archives can be found at: http://metaforclimate.eu/trac/browser/CIM.

The CIM is defined at the conceptual level, in UML, first.  After the CONCIM structure has been agreed upon, it gets translated into the APPCIM, a set of XML Schemas. 

The CIM is broken up into several packages for ease of development.  Each of these has its own subdirectory where related files (schema files, images, and related documentation) are stored.  This includes UML diagrams in PNG format.

All of the packages are developed together as a single Enterprise Architect (EA) project.  This project is stored in the top-level cim.xmi file.  As changes to the UML ocurr, this file gets overwritten.

The concim2appcim.xsl file can be used to transform that cim.xmi file to a series of XSD files defining the APPCIM.  The CIM makes use of some external schemas (xlink, gmd, gml, etc.).  These can be found in the "external_schemas" project stored above the CIM SVN Repository.

Be sure to specify the "namespace" and "version" paramters for that transformation. You can also use set "debug" to "true" to print out what the code is doing.  And the "sort-attributes" parameter sorts UML attributes alphabetically instead of in the order they appear in the XMI file (do not do this unless you have a very good reason).

Manipulating the CIM APPCIM, including using it to validate CIM instances, can be a slow process.  To expedite this process, ensure that all the xsd files (including the external schemas) are at a location known to your validator - either on the local filesystem or online someplace.  A sample "oasis_catalog.xml" file has been provided for this; most modern XML tools are oasis_catalog-aware.

**********

upon checking out a new working copy...

01) create a new Enterprise Architect Project (cim.eap)
02) select no models by default
03) create a new top-level view called "Domain Model"
04) import cim.xmi into that view
05) create a new top-level view called "Externally Goverend Packages"
06) create a (sub)package for that view called "Hollow World"
07) import ../external_schemas/ISO19100.xmi into that view
08) import ../external_schemas/CommonUsagePackages.xmi into that view
09) import ../external_schemas/SWE.xmi into that view
10) check that everything worked by looking at the shared package diagram; the top should contain lots of classes imported from ISO19100
11) save the project
