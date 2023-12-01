import os
import arrays

fn main() {
    lines := os.read_lines('input_1') or {
	return
    }
    mut elves := []int{}
    mut sum := 0
    for line in lines {
	if line == '' {
	    elves << sum
	    sum = 0
	    continue
	}
	sum += line.int()
    }
    println(arrays.max(elves) or {return})
}
