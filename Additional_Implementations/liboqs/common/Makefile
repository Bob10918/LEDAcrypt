# This Makefile can be used with GNU Make or BSD Make

CC = gcc
# CC = clang

LIB = common.o

SOURCES = aes.c fips202.c nistseedexpander.c randombytes.c sha2.c sp800-185.c

HEADERS = aes.h fips202.h nistseedexpander.h randombytes.h sha2.h sp800-185.h

CFLAGS  = -O3 -std=c99 -Wall -Wextra -Wpedantic -Werror -Wmissing-prototypes \
      -march=native -g3

all: $(LIB)

$(LIB): $(SOURCES) $(HEADERS)
	$(CC) $(CFLAGS) -c $^

clean:
	$(RM) $(OBJECTS)
	$(RM) $(LIB)