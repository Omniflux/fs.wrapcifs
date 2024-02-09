gendazpack
==========

``gendazpack`` is a DAZ Studio content package generator.

Supported Python versions
-------------------------

- Python 3.12

Usage
-----

``gendazpack [-h] [-g GLOBAL_ID] [-u URL] [-p PREFIX] [-s SKU] [-I ID] [-S STORE]
           [-n NAME] [-t TAGS [TAGS ...]] [-a AUTHORS [AUTHORS ...]]
           [-d DESCRIPTION] [-i IMAGE] [-r README] [-v] content_location``

positional arguments:
  content_location          Content directory

options:
  -h, --help            show this help message and exit
  -g GLOBAL_ID, --global-id GLOBAL_ID
                        Product Global ID
  -u URL, --url URL     URL for product information
  -p PREFIX, --prefix PREFIX
                        Source Prefix
  -s SKU, --sku SKU     Product SKU
  -I ID, --id ID        Package ID
  -S STORE, --store STORE
                        Product Store
  -n NAME, --name NAME  Product [Part] Name
  -t TAGS [TAGS ...], --tags TAGS [TAGS ...]
                        Tags
  -a AUTHORS [AUTHORS ...], --authors AUTHORS [AUTHORS ...]
                        Authors
  -d DESCRIPTION, --description DESCRIPTION
                        Product Description
  -i IMAGE, --image IMAGE
                        Product Image
  -r README, --readme README
                        Product ReadMe
  -v, --verbose         enable verbose output

.. code:: 

    E:\> gendazpack --sku 000000 --name "My Product" D:\ContentToPackage

    E:\> gendazpack --prefix ROSITY --sku 000000 --store Renderosity --name "Some Product" --image D:\ProductImage.png --readme D:\ProductReadme.pdf  D:\ContentToPackage

    E:\> gendazpack --url https://www.renderosity.com/marketplace/products/000000/some-product D:\ContentToPackage

License
-------

This module is published under the MIT license.