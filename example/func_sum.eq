int a := 10
int b := 20

def sum {
    write => str(a + b) + '\n'
}

def_sum

int a := 21
int b := 10

def_sum