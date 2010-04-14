This is the CIM SVN Repository.  It is where CIM development is coordinated.

The CIM is broken up into several UML packages for ease of development.  Each of these is stored in its own subdirectory as an XMI file.  Additionally, any image files that developers feel are useful are saved as PNGs.  

The concim2appcim.xsl file can be used to transform the (top-level) cim.xmi file to a series of XSD files defining the APPCIM.  The CIM makes use of some external schemas (xlink, gmd, gml, etc.).  These can be found in the "external_schemas" project w/in this SVN repository.

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
