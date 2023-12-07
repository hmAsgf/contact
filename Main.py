from ContactView import ContactView

class Main:
  
  def __init__(self):
    self.run()

  @staticmethod
  def run():
    while True:
      opsi = ContactView.menu()

      if opsi == '1':
        ContactView.show()

      elif opsi == '2':
        ContactView.add()

      elif opsi == '3':
        ContactView.edit()

      elif opsi == '4':
        ContactView.remove()
      
      elif opsi == '0':
        break

      else:
        continue        

if __name__ == '__main__':
  Main()