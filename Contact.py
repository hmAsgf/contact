from pymongo import MongoClient
from pymongo.collection import ObjectId

class Contact:
  CLIENT = MongoClient('mongodb://localhost:27017/')
  DATABASE = CLIENT['contactApp']
  COLLECTION = DATABASE['contacts']

  @staticmethod
  def create(data: dict):
    try:
      Contact.COLLECTION.insert_one(data)
      return 'KONTAK BERHASIL DITAMBAHKAN!'
    except:
      return 'KONTAK GAGAL DITAMBAHKAN!'

  @staticmethod
  def read():
    return [contact for contact in Contact.COLLECTION.find()]

  @staticmethod
  def update(id: ObjectId, data: dict):
    try:
      Contact.COLLECTION.update_one({'_id': id}, {'$set': data})
      return 'KONTAK BERHASIL DIPERBARUI!'
    except:
      return 'KONTAK GAGAL DIPERBARUI!'

  @staticmethod
  def delete(id: ObjectId):
    try:
      Contact.COLLECTION.delete_one({'_id': id})
      return 'KONTAK BERHASIL DIHAPUS!'
    except:
      return 'KONTAK GAGAL DIHAPUS!'