# This Makefile can be used with GNU Make or BSD Make

CC = gcc
# CC = clang

LIB = ledacrypt

HEADERS = H_Q_matrices_generation.h djbsort.h gf2x_limbs.h \
      gf2x_arith.h rng.h gf2x_arith_mod_xPplusOne.h \
      api.h niederreiter.h niederreiter_keygen.h bf_decoding.h niederreiter_decrypt.h \
      qc_ldpc_parameters.h dfr_test.h niederreiter_encrypt.h \
      test_kem.h aes256.h timing_and_stat.h

OBJECTS = aes256.o bf_decoding.o dfr_test.o djbsort.o gf2x_arith.o gf2x_arith_mod_xPplusOne.o \
	  H_Q_matrices_generation.o kem.o main_kem.o niederreiter_decrypt.o niederreiter_encrypt.o \
	  niederreiter_keygen.o rng.o test_kem.o \
	  aes.o fips202.o nistseedexpander.o randombytes.o

EXTRAFLAGS = -DCONSTANT_TIME=1 -DN0=2 -DCATEGORY=1 -DDFR_SL_LEVEL=0 -lrt -lm

CFLAGS  = -O3 -std=c99 -Wall -Wextra -Wpedantic -Werror -Wmissing-prototypes \
      -march=native -g3 -I../common/ -I/usr/include $(EXTRAFLAGS)


all: $(LIB)

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c -o $@ $<

$(LIB): $(OBJECTS)
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	$(RM) $(OBJECTS)
	$(RM) $(LIB)

#$(LIB): $(SOURCES) $(HEADERS)
#	$(CC) $(CFLAGS)   -o $@ $^
#
#clean:
#	$(RM) $(OBJECTS)
#	$(RM) $(LIB)