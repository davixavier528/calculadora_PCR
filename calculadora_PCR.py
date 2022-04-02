# a reação de PCR usada aqui é proveniente de um protocolo de genotipagem de camundongos das linhagens STAT, CD11c-Cre e hACE2
# consequentemente (e obviamente), possui certas especificidades que devem ser modificadas para atender a sua necessidade

reação = int(input("Insira o número referente à reação que você deseja calulcar o MIX: se STAT1 ou STAT3, insira 1; se STAT5, insira 2; se CD11c-Cre, insira 3; se hACE2, insira 4: "))
NúmeroDeCamundongos = int(input("Quantos camundongos você precisa genotipar? "))

if reação == 1: 
    miliQ = 13.8
    buffer = 2
    dNTP = 0.4
    MgCl2 = 0.6
    Primer1 = 1
    Primer2 = 1
    TaqPolimerase = 0.2
    DNA = 1
    print()
    print("O seu MIX precisará de:")
    print()
    print("mili Q =", miliQ * (NúmeroDeCamundongos + 2), "ul")
    print("buffer =", buffer * (NúmeroDeCamundongos + 2), "ul") 
    print("dNTP =", dNTP * (NúmeroDeCamundongos + 2), "ul")
    print("MgCl2 =", MgCl2 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 1 =", Primer1 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 2 =", Primer2 * (NúmeroDeCamundongos + 2), "ul")
    print("Taq Polimerase =", TaqPolimerase * (NúmeroDeCamundongos + 2), "ul")
    print("DNA = 1ul de cada amostra")
    print("Volume final =", (miliQ + buffer + dNTP + MgCl2 + Primer1 + Primer2 + TaqPolimerase) * (NúmeroDeCamundongos + 2))

if reação == 2: 
    miliQ = 12.8
    buffer = 2
    dNTP = 0.4
    MgCl2 = 0.6
    Primer1 = 1
    Primer2 = 1
    Primer3 = 1
    TaqPolimerase = 0.2
    DNA = 1
    print()
    print("O seu MIX precisará de:")
    print()
    print("mili Q =", miliQ * (NúmeroDeCamundongos + 2), "ul")
    print("buffer =", buffer * (NúmeroDeCamundongos + 2), "ul") 
    print("dNTP =", dNTP * (NúmeroDeCamundongos + 2), "ul")
    print("MgCl2 =", MgCl2 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 1 =", Primer1 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 2 =", Primer2 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 3 =", Primer2 * (NúmeroDeCamundongos + 2), "ul")
    print("Taq Polimerase =", TaqPolimerase * (NúmeroDeCamundongos + 2), "ul")
    print("DNA = 1ul de cada amostra")
    print("Volume final =", (miliQ + buffer + dNTP + MgCl2 + Primer1 + Primer2 + Primer3 + TaqPolimerase) * (NúmeroDeCamundongos + 2))

if reação == 3: 
    miliQ = 11.8
    buffer = 2
    dNTP = 0.4
    MgCl2 = 0.6
    Primer1 = 1
    Primer2 = 1
    Primer3 = 1
    Primer4 = 1
    TaqPolimerase = 0.2
    DNA = 1
    print()
    print("O seu MIX precisará de:")
    print()
    print("mili Q =", miliQ * (NúmeroDeCamundongos + 2), "ul")
    print("buffer =", buffer * (NúmeroDeCamundongos + 2), "ul") 
    print("dNTP =", dNTP * (NúmeroDeCamundongos + 2), "ul")
    print("MgCl2 =", MgCl2 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 1 =", Primer1 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 2 =", Primer2 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 3 =", Primer2 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 4 =", Primer2 * (NúmeroDeCamundongos + 2), "ul")
    print("Taq Polimerase =", TaqPolimerase * (NúmeroDeCamundongos + 2), "ul")
    print("DNA = 1ul de cada amostra")
    print("Volume final =", (miliQ + buffer + dNTP + MgCl2 + Primer1 + Primer2 + Primer3 + Primer4 + TaqPolimerase) * (NúmeroDeCamundongos + 2))

if reação == 4: 
    miliQ = 12.8
    buffer = 2
    DMSO = 1
    dNTP = 0.4
    MgCl2 = 0.6
    Primer1 = 1
    Primer2 = 1
    Primer3 = 1
    TaqPolimerase = 0.2
    DNA = 1
    print()
    print("O seu MIX A precisará de:")
    print()
    print("mili Q =", miliQ * (NúmeroDeCamundongos + 2), "ul")
    print("buffer =", buffer * (NúmeroDeCamundongos + 2), "ul")
    print("DMSO =", DMSO * (NúmeroDeCamundongos + 2), "ul")
    print("dNTP =", dNTP * (NúmeroDeCamundongos + 2), "ul")
    print("MgCl2 =", MgCl2 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 579 =", Primer1 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 580 =", Primer2 * (NúmeroDeCamundongos + 2), "ul")
    print("Taq Polimerase =", TaqPolimerase * (NúmeroDeCamundongos + 2), "ul")
    print("DNA = 1ul de cada amostra")
    print("Volume final =", (miliQ + buffer + dNTP + MgCl2 + Primer1 + Primer2 + TaqPolimerase) * (NúmeroDeCamundongos + 2))
    print()
    print("O seu MIX B precisará de:")
    print()
    print("mili Q =", miliQ * (NúmeroDeCamundongos + 2), "ul")
    print("buffer =", buffer * (NúmeroDeCamundongos + 2), "ul")
    print("DMSO =", DMSO * (NúmeroDeCamundongos + 2), "ul")
    print("dNTP =", dNTP * (NúmeroDeCamundongos + 2), "ul")
    print("MgCl2 =", MgCl2 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 578 =", Primer1 * (NúmeroDeCamundongos + 2), "ul")
    print("Primer 579 =", Primer2 * (NúmeroDeCamundongos + 2), "ul")
    print("Taq Polimerase =", TaqPolimerase * (NúmeroDeCamundongos + 2), "ul")
    print("DNA = 1ul de cada amostra")
    print("Volume final =", (miliQ + buffer + dNTP + MgCl2 + Primer1 + Primer2 + TaqPolimerase) * (NúmeroDeCamundongos + 2))

input()