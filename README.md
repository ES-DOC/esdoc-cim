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


What are the contents of esdoc-cim ?
--------------------------------------

The CIM is broken up into several UML packages for ease of development.  Each of these has its own subdirectory where related files are stored.

    \activity	CIM Activity package
    \data	CIM Data package
    \grids	CIM Grids package
    \quality	CIM Quality package
    \shared	CIM Shared package
    \software	CIM Software package
    \docs	HTML documentation

ConCIM files are stored as UML.  AppCIM files are stored as XSD.  Additionally, there are structure diagrams of relevant bits of the CIM stored as PNG.  

There are also XSL files used to, among other things, convert from the ConCIM to AppCIM.

<!-- TODO: Add further information

Further Information ?
--------------------------------------

Please refer to the documentation for further information: TODO

-->
