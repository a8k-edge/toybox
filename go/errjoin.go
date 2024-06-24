package main

import (
	"errors"
	"fmt"
	"io"
	"log"
	"os"
)

func ReadFiles(paths []string) ([][]byte, error) {
	var errs error
	var contents [][]byte

	if len(paths) == 0 {
		// Create a new error with fmt.Errorf() (but without using %w):
		return nil, fmt.Errorf("no paths provided: paths slice is %v", paths)
	}

	for _, path := range paths {
		content, err := ReadFile(path)
		if err != nil {
			errs = errors.Join(errs, fmt.Errorf("reading %s failed: %w", path, err))
			continue
		}
		contents = append(contents, content)
	}

	return contents, errs
}

func ReadFile(path string) ([]byte, error) {
	if path == "" {
		// Create an error with errors.New()
		return nil, errors.New("path is empty")
	}
	f, err := os.Open(path)
	if err != nil {
		// Wrap the error.
		// If the format string uses %w to format the error,
		// fmt.Errorf() returns an error that has the
		// method "func Unwrap() error" implemented.
		return nil, fmt.Errorf("open failed: %w", err)
	}
	defer f.Close()

	buf, err := io.ReadAll(f)
	if err != nil {
		return nil, fmt.Errorf("read failed: %w", err)
	}
	return buf, nil
}

func main() {
	_, errs := ReadFiles([]string{
		"1.txt",
		"2.txt",
		"3.txt",
		"",
	})
	log.Printf("%v", errs)
}
