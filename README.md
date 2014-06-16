esdoc-cim
=========

Repository defining the Metafor Common Information Model.


==================================================

What is ES-DOC ?
--------------------------------------

ES-DOC stands for Earth Science - Documentation.  It's goal is to provide software tools and services in order to support the distribution of earth science documentation.


What is the CIM ?
--------------------------------------

Metafor was a European project tasked with defining a metadata standard for describing scientific processes, particularly climate modelling processes.  This metadata standard came to be known as the CIM (Common Information Model).


What is esdoc-cim ?
-------------------

esdoc-cim contains information artefacts defining the CIM on the conceptual level (known as ConCIM).  It stores UML models of the CIM in XMI format along with an HTML graphical representations of the model.


What are the contents of esdoc-questionnaire ?
--------------------------------------

The CIM is broken up into several UML packages for ease of development.  Each of these has its own subdirectory where related files are stored.  Currently, this includes UML diagrams in PNG format.

All of the packages are developed together as a single Enterprise Architect (EA) project.  This project is stored in the top-level cim.xmi file.  As changes to the UML ocurr, this file gets overwritten.

The concim2appcim.xsl file can be used to transform that cim.xmi file to a series of XSD files defining the APPCIM.  The CIM makes use of some external schemas (xlink, gmd, gml, etc.).  These can be found in the "external_schemas" project w/in this repository.
Be sure to specify the "namespace" and "version" paramters for that transformation (you can also use set debug to "true" to print out what the code is doing).


    \activity	CIM Activity package
    \data	CIM Data package
    \grids	CIM Grids package
    \quality	CIM Quality package
    \shared	CIM Shared package
    \software	CIM Software package
    \docs	HTML representation


<!-- TODO: Add further information

Further Information ?
--------------------------------------

Please refer to the documentation for further information: TODO

-->
