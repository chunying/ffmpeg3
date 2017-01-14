all:
	@./ffbuild.py

clean:
	rm -rf build

cleanall: clean
	rm -rf cached
