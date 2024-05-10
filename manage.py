def topic(x):
  if x == 1:
      a = open("intel/Math.txt", "r")
  elif x == 2:
      a = open("intel/Phy.txt", "r")
  elif x == 3:
      a = open("intel/Chem.txt", "r")
  elif x == 4:
      a = open("intel/Bio.txt", "r")
  b = a.read()
  return b


def combine(cha, rep):

  if rep == 1:
      rep = "Questions with answers"
  elif rep == 2:
      rep = "Notes"
  elif rep == 3:
      rep = "Summary"
  elif rep == 4:
      rep = "All"

  vfr = str("Genterate " + rep + " of " + cha)
  print(vfr)
  return vfr


def save(a, filename, rep):
  if rep == 1:
      de = "Qna/"
  elif rep == 2:
      de = "Notes/"
  elif rep == 3:
      de = "Summary/"
  x = "Output/" + de + filename + ".txt"
  z = open(x, "w")
  z.write(a)
