package day04

import (
	"fmt"
	"os"
	s "strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func horizontal(input_str []string) int {
	// search XMAS or SAMX horizontaly
	xmas := 0
	samx := 0
	for i := range len(input_str) {
		xmas += s.Count(input_str[i], "XMAS")
		samx += s.Count(input_str[i], "SAMX")
	}
	return xmas + samx
}

func vertical(input_str []string) int {
	// search XMAS or SAMX vertically
	xmas := 0
	samx := 0
	for i := range len(input_str) - 3 {
		for j := range len(input_str[i]) {
			if string(input_str[i][j]) == "X" && string(input_str[i + 1][j]) == "M" && string(input_str[i + 2][j]) == "A" && string(input_str[i + 3][j]) == "S" {
				xmas += 1
			} else if string(input_str[i][j]) == "S" && string(input_str[i + 1][j]) == "A" && string(input_str[i + 2][j]) == "M" && string(input_str[i + 3][j]) == "X" {
				samx += 1
			}
		}
	}
	return xmas + samx
}

func diagonal(input_str []string) int {
	// search XMAS or SAMX diagonaly
	xmas := 0
	samx := 0
	for i := range len(input_str) - 3 {
		for j := range len(input_str[i]) - 3 {
			// right diagonal
			if string(input_str[i][j]) == "X" && string(input_str[i + 1][j + 1]) == "M" && string(input_str[i + 2][j + 2]) == "A" && string(input_str[i + 3][j + 3]) == "S" {
				xmas += 1
			} else if string(input_str[i][j]) == "S" && string(input_str[i + 1][j + 1]) == "A" && string(input_str[i + 2][j + 2]) == "M" && string(input_str[i + 3][j + 3]) == "X" {
				samx += 1
			}
			// left diagonal
			if string(input_str[i][j + 3]) == "X" && string(input_str[i + 1][j + 2]) == "M" && string(input_str[i + 2][j + 1]) == "A" && string(input_str[i + 3][j]) == "S" {
				xmas += 1
			} else if string(input_str[i][j + 3]) == "S" && string(input_str[i + 1][j + 2]) == "A" && string(input_str[i + 2][j + 1]) == "M" && string(input_str[i + 3][j]) == "X" {
				samx += 1
			}
		}
	}
	return xmas + samx
}

func diagonal_mas(input_str []string) int {
	// search MAS or SAM diagonaly
	mas := 0
	sam := 0
	for i := range len(input_str) - 2 {
		for j := range len(input_str[i]) - 2 {
			if string(input_str[i][j]) == "M" && string(input_str[i + 1][j + 1]) == "A" && string(input_str[i + 2][j + 2]) == "S" {
				if string(input_str[i][j + 2]) == "M" && string(input_str[i + 1][j + 1]) == "A" && string(input_str[i + 2][j]) == "S" {
					mas += 1
				} else if string(input_str[i][j + 2]) == "S" && string(input_str[i + 1][j + 1]) == "A" && string(input_str[i + 2][j]) == "M" {
					sam += 1
				}
			} else if string(input_str[i][j]) == "S" && string(input_str[i + 1][j + 1]) == "A" && string(input_str[i + 2][j + 2]) == "M" {
				if string(input_str[i][j + 2]) == "M" && string(input_str[i + 1][j + 1]) == "A" && string(input_str[i + 2][j]) == "S" {
					mas += 1
				} else if string(input_str[i][j + 2]) == "S" && string(input_str[i + 1][j + 1]) == "A" && string(input_str[i + 2][j]) == "M" {
					sam += 1
				}
			}
		}
	}
	return mas + sam
}

func Run() {
	dat, err := os.ReadFile("day04/cer_sea_input.txt")
	check(err)
	raw_input := s.Split(string(dat), "\n")
	fmt.Println(horizontal(raw_input) + vertical(raw_input) + diagonal(raw_input))
	fmt.Println(diagonal_mas(raw_input))
}
