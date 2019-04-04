#!/bin/bash
set -ue
trap 'rm -f $THIS_DIR/issagen.tar.gz' EXIT
readonly THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-${(%):-%N}}")" && pwd)"
tar zcvf "${THIS_DIR}"/issagen.tar.gz -C "${THIS_DIR}" bin .tar2package.yml
docker run -i greymd/tar2rpm < "${THIS_DIR}"/issagen.tar.gz > "${THIS_DIR}/pkg/issagen.rpm"
docker run -i greymd/tar2deb < "${THIS_DIR}"/issagen.tar.gz > "${THIS_DIR}/pkg/issagen.deb"
