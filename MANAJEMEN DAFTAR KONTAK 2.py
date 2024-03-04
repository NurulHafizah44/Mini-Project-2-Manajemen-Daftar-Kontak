class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ContactManager:
    def __init__(self):
        self.head = None

    def create_contact(self, name, phone_number, email):
        new_contact = Node({'name': name, 'phone_number': phone_number, 'email': email})
        if not self.head:
            self.head = new_contact
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_contact
        print("Kontak berhasil ditambahkan.")

    def read_contacts(self):
        current = self.head
        if not current:
            print("Daftar kontak kosong.")
        else:
            print("Daftar Kontak:")
            while current:
                contact = current.data
                print(f"Nama: {contact['name']}, No. Telepon: {contact['phone_number']}, Email: {contact['email']}")
                current = current.next

    def update_contact(self, index, name, phone_number, email):
        current = self.head
        position = 0
        while current and position != index:
            current = current.next
            position += 1
        if not current:
            print("Indeks kontak tidak valid.")
        else:
            current.data = {'name': name, 'phone_number': phone_number, 'email': email}
            print("Kontak berhasil diperbarui.")

    def delete_contact(self, index):
        current = self.head
        if index == 0:
            self.head = current.next
            del current
            print("Kontak berhasil dihapus.")
            return
        position = 0
        while current and position != index - 1:
            current = current.next
            position += 1
        if not current or not current.next:
            print("Indeks kontak tidak valid.")
            return
        deleted_node = current.next
        current.next = deleted_node.next
        del deleted_node
        print("Kontak berhasil dihapus.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nPilihan Menu:")
        print("1. Tambah Kontak")
        print("2. Lihat Daftar Kontak")
        print("3. Perbarui Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5): ")

        if choice == '1':
            name = input("Masukkan nama kontak: ")
            phone_number = input("Masukkan nomor telepon kontak: ")
            email = input("Masukkan email kontak: ")
            contact_manager.create_contact(name, phone_number, email)
        elif choice == '2':
            contact_manager.read_contacts()
        elif choice == '3':
            index = int(input("Masukkan indeks kontak yang akan diperbarui: "))
            name = input("Masukkan nama baru: ")
            phone_number = input("Masukkan nomor telepon baru: ")
            email = input("Masukkan email baru: ")
            contact_manager.update_contact(index, name, phone_number, email)
        elif choice == '4':
            index = int(input("Masukkan indeks kontak yang akan dihapus: "))
            contact_manager.delete_contact(index)
        elif choice == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
