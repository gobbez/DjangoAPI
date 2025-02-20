<h2>DJANGO CRUD METHODS</h2>
Django has ready-to-go methods for crud (for Example table).

<h3>✅ CREATE (add new record)</h3>
method 1: 
Example.objects.create(text="Ciao", number=10)

method 2:
nuovo = Example(text="Hello", number=42)
nuovo.save()

<h3>🔍 READ (Select data)</h3>
all data:
Example.objects.all()

single record:
Example.objects.get(id=1) 

filter results:
Example.objects.filter(text="Ciao")  

<h3>✏️ UPDATE (Modify a record)</h3>
record = Example.objects.get(id=1)
record.text = "Nuovo testo"
record.save()  

modify more records together:
Example.objects.filter(number=10).update(text="Aggiornato")

<h3>🗑️ DELETE (Delete a record)</h3>
record = Example.objects.get(id=1)
record.delete()

delete more records:
Example.objects.filter(number=10).delete()