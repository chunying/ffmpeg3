all:
	@./run.py

clean:
	rm -rf build

cleanall: clean
	rm -rf cached
