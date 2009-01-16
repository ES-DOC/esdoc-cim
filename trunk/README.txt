This is the CIM SVN Repository.  It is where CIM development is coordinated.

The CIM is broken up into several UML packages for ease of development.  Each of these is stored in its own subdirectory as an XMI file.  Additionally, any image files that developers feel are useful are saved as PNGs.  

The concim2appcim.xsl file can be used to transform the (top-level) cim.xmi file to a series of XSD files defining the APPCIM.  The CIM makes use of some external schemas (xlink, gmd, gml, etc.).  These can be found in the "external_schemas" project w/in this SVN repository.
