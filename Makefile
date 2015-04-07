SRC = $(wildcard *.cpp)
OUT = $(SRC:.cpp=)

CXXFLAGS = -O3 -pedantic -Wall -Wextra

all: $(OUT)

clean:
	$(RM) $(OUT)

.PHONY: clean
