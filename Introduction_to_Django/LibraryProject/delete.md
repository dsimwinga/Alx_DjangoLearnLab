book.delete()

# Verify deletion
print(Book.objects.all().count())  # Expected output: 0