#!/bin/bash

# Start up script for setting up environment on Ubuntu 20.04 LTS

export PKGNAME='bnn_mcmc_examples'
export PYVERSION='3.7'
export CONDADIR="$HOME/opt/continuum/miniconda/miniconda3"
export PYPKGDIR="$HOME/opt/python/packagesss"
export CONDAENV="$CONDADIR/envs/$PKGNAME"
export CONDABIN="$CONDADIR/bin/conda"
export CONDASCRIPT='Miniconda3-latest-Linux-x86_64.sh'
export PKGURL="https://github.com/papamarkou/$PKGNAME.git"
export PKGDEVREQS="$PYPKGDIR/$PKGNAME/installation/requirements.txt"

sudo apt-get update

sudo apt-get install tree

wget https://repo.anaconda.com/miniconda/$CONDASCRIPT
chmod u+x $CONDASCRIPT

$SHELL $CONDASCRIPT -b -p $CONDADIR

$CONDABIN create -n $PKGNAME -y python=$PYVERSION

$CONDABIN init $(basename $SHELL)
$CONDABIN config --set auto_activate_base false

mkdir -p $PYPKGDIR

git -C $PYPKGDIR clone "https://github.com/papamarkou/kanga.git"
$CONDABIN run -p $CONDAENV pip install -e "$PYPKGDIR/kanga" -r "$PYPKGDIR/kanga/requirements.txt"

git -C $PYPKGDIR clone "https://github.com/papamarkou/eeyore.git"
$CONDABIN run -p $CONDAENV pip install -e "$PYPKGDIR/eeyore" -r "$PYPKGDIR/eeyore/installation/requirements.txt"

git -C $PYPKGDIR clone $PKGURL
$CONDABIN run -p $CONDAENV pip install -e "$PYPKGDIR/$PKGNAME" -r $PKGDEVREQS

rm $HOME/$CONDASCRIPT
