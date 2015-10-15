#!/bin/bash

#script taken from https://github.com/footley/gedit-wordcount-plugin

if [ ! -d ~/.local/share/gedit ]; then
	mkdir ~/.local/share/gedit
fi

if [ ! -d ~/.local/share/gedit/plugins ]; then
	mkdir ~/.local/share/gedit/plugins
fi

echo remove any old version
rm ~/.local/share/gedit/plugins/wc.*

echo copy plugin files
cp wc.plugin ~/.local/share/gedit/plugins/
cp wc.py ~/.local/share/gedit/plugins/
