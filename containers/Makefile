# Makefile for container needs
# Author: Ben Trachtenberg
# Version: 1.0.0
#

.PHONY: build-container

info:
	@echo "make options"
	@echo "    build-container             To build the container"


build-container:
	@echo "Building the container with build_branch=$(build_branch)"

	@podman build --ssh=default --build-arg=build_branch=$(build_branch) -t django-portfolio:latest -t django-portfolio:$(build_branch) -f Containerfile




