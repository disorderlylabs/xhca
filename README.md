# Accelerate Human Cell Atlas (XHCA)
-------------------------------

### Overview
____________
This is a repository for a collaborative project between Peter Alvaro's lab, Josh Stuart's lab, and Seagate.
The overall goal is to research improvements in storage systems and smart disks to improve data storage for
bioinformatics applications--especially the Human Cell Atlas.

Figure 1, below, highlights three primary components: (1) the scientific application, (2) the access library
interface, and (3) the storage system interface. The figure also shows how these components are related, and
how they can be grouped into file format (access library) and storage system (object store). In short, one
of the goals of this project is to explore how to provide high-level information from the application to
the storage system so that the storage system can choose optimal low-level policies and mechanisms to support
high-level abstractions and computation.

<figure>
  <img src="assets/data-access-path/overview.png" height="600" margin-left:"auto" />
  <figcaption text-align:"middle">
    <strong>Figure 1</strong>
    Overview of components of the data access path and annotated interactions.
  </figcaption>
</figure>
