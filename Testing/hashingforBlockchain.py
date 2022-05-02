# This is example of Hasing using SHA256 Algorithm
import hashlib

A_Stirng = "this string holds important and private information"

# Hash a single string with hashlib.sha256
HasedString = hashlib.sha256(A_Stirng.encode('utf-8')).hexdigest()

print(HasedString)  # Returns: 4e7d696bce894548dded72f6eeb04e8d625cc7f2afd08845824a4a8378b428d1
