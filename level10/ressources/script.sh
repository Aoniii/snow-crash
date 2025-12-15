#!/bin/bash

touch /tmp/fake;

while true;
do
	ln -sf /tmp/fake /tmp/faketoken;
	ln -sf /home/user/level10/token /tmp/faketoken;
done
