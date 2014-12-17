# INSTALLATION INSTRUCTIONS

The following instructions describe how to work with the CIM. 

The CIM is broken up into several packages for ease of development.  Each of these has its own subdirectory where related files are stored.  This includes structural diagrams in PNG format.

All of the packages are developed together as a single Enterprise Architect (EA) project.  This project is stored in the top-level cim.xmi file.  As changes to the UML ocurr, this file gets overwritten.

The "concim2appcim.xsl" file can be used to transform cim.xmi into a series of XSD files defining the AppCIM.  Be sure to specify the "namespace" and "version" parameters for that transformation.

Additionally, the CIM makes use of several external schemas (xlink, gmd, gml, etc.).  These should be located in an "external_schemas" directory.

## PRE-REQUISITES

* Enterprise Architect
* an XML editor (Oxygen is recommended)
* libXML
* Python

## USE

upon checking out a new branch...

01. create a new Enterprise Architect Project (cim.eap)
02. select no models by default
03. create a new top-level view called "Domain Model"
04. import cim.xmi into that view
05. create a new top-level view called "Externally Goverend Packages"
06. create a (sub)package for that view called "Hollow World"
07. import ../external_schemas/ISO19100.xmi into that view
08. import ../external_schemas/CommonUsagePackages.xmi into that view
09. import ../external_schemas/SWE.xmi into that view
10. check that everything worked by looking at the shared package diagram; the top should contain lots of classes imported from ISO19100
11. save the project
