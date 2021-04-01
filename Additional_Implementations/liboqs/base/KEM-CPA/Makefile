CC = gcc
# CC = clang

SANITIZE = ""
LIB = ledacrypt

EXTRAFLAGS = -DCONSTANT_TIME=1 -DN0=2 -DCATEGORY=1 -DDFR_SL_LEVEL=0

CFLAGS  = -O3 -std=c99 -Wall -Wextra -Wpedantic -Werror -Wmissing-prototypes \
      -march=native -g3 -I../../common $(EXTRAFLAGS)