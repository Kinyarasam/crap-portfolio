#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

# see also ".mailmap" fo how email addresses and names are deduplicated

{
    cat <<- 'EOH'
		These individuals contriuted to the hbnb project in this repository

	EOH
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
