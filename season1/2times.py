adad = int(input())

adad1 = str(adad // 100)
adad2 = str((adad // 10) % 10)
adad3 = str(adad % 10)
adad_akhar = int(adad3 + adad2 + adad1) * 2
print(adad_akhar)
