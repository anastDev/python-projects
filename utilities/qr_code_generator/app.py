from scripts.generate_qr import *

def main():
  print("=== QR Code Generator ===")
  url = input("Enter URL: ")
  file_path = input("Enter output filename (default: qr_code.png): ").strip()
    
  if not file_path:
    file_path = "qr_code.png"
    
  if not file_path.endswith('.png'):
    file_path += '.png'
    
  generate_qr(url, file_path)

  
if __name__ == "__main__":
  main()