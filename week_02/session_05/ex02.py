import sys
print("Алдааны мессеж", file=sys.stderr)

sys.stdout.write("Энэ бол стандарт гаралт\n")

sys.stderr.write("Энэ бол алдааны мессеж\n")

print("Ямар нэгэн зүйл бичээд Enter дарна уу:")
user_input = sys.stdin.readline()/strip()
print(f"Та бичсэн: {user_input}")

