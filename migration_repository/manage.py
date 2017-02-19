#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(debug='False',
         repository='migration_repository',
         url='postgres://async-lab@postgres/async-lab?password=async-lab')
