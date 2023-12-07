from Contact import Contact

class ContactView:
  @staticmethod
  def menu():
    print('='*50)
    print('''[1] LIHAT KONTAK
[2] TAMBAH KONTAK
[3] PERBARUI KONTAK
[4] HAPUS KONTAK
[0] KELUAR''')
    print('-'*50)
    opsi = input('PILIH MENU: ')
    print('='*50)
    return opsi

  @staticmethod
  def show():
    print('LIHAT KONTAK')
    for contact in Contact.read():
      print('-'*50)
      print(f"NAMA LENGKAP  : {contact['name']['first'] + ' ' + contact['name']['last']}")
      print(f"NOMOR TELEPON : {contact['phone']}")
      print(f"EMAIL         : {contact['email']}")

  @staticmethod
  def add():
    print('TAMBAH KONTAK')
    print('-'*50)

    firstname = input('NAMA DEPAN    : ')
    lastname = input('NAMA BELAKANG : ')
    phone = input('NOMOR TELEPON : ')
    email = input('EMAIL         : ')
    contact = {
      'name': {
        'first': firstname,
        'last': lastname
      },
      'phone': phone,
      'email': email
    }
    print('-'*50)
    print(Contact.create(contact))

  @staticmethod
  def edit():
    print('PERBARUI KONTAK')
    print('-'*50)
    print('0. Keluar')
    for i, contact in enumerate(Contact.read()):
      print('-'*50)
      print(f"{i+1}. {contact['name']['first'] + ' ' + contact['name']['last']}")
    
    while True: 
      print('-'*50)
      index = int(input('PILIH KONTAK YANG INGIN DIPERBARUI: '))
      if index == 0:
        break
      elif index > 0 and index <= len(Contact.read()):
        contact = Contact.read()[index-1]
        _id = contact['_id']
        print('-'*50)
        firstname = input(f"NAMA DEPAN ({contact['name']['first']}) : ")
        lastname = input(f"NAMA BELAKANG ({contact['name']['last']}) : ")
        phone = input(f"NOMOR TELEPON ({contact['phone']}) : ")
        email = input(f"EMAIL ({contact['email']}) : ")

        if firstname: contact['name']['first'] = firstname
        if lastname: contact['name']['last'] = lastname
        if phone: contact['phone'] = phone
        if email: contact['email'] = email
        print('-'*50)
        print(Contact.update(_id, contact))
        break

  @staticmethod
  def remove():
    print('HAPUS KONTAK')
    print('-'*50)
    print('0. Keluar')
    for i, contact in enumerate(Contact.read()):
      print('-'*50)
      print(f"{i+1}. {contact['name']['first'] + ' ' + contact['name']['last']}")
    
    while True: 
      print('-'*50)
      index = int(input('PILIH KONTAK YANG INGIN DIHAPUS: '))
      if index == 0:
        break
      elif index > 0 and index <= len(Contact.read()):
        contact = Contact.read()[index-1]
        _id = contact['_id']
        print('-'*50)
        print(Contact.delete(_id))
        break