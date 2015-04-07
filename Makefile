SRC = $(wildcard *.cpp)
OUT = $(SRC:.cpp=)

CXXFLAGS = -std=c++11 -O3 -pedantic -Wall -Wextra -Werror
LDLIBS = -lboost_program_options

all: $(OUT)

clean:
	$(RM) $(OUT)

.PHONY: clean
