import os
import shutil

nb = 0
listeee = []


class Dothis:
    def __init__(self, command, parameter):
        self.command = command
        self.parameter = parameter

    def get_command(self):
        return self.command

    def get_parameter(self):
        return self.parameter


class Action(Dothis):
    # this object will do some things with a file ( .txt is more adapted, but programs are
    # more adapted for executation :-) )
    def __init__(self, command, file, parameter, mode, ccn, ce, cm, arg, arg2, arg3):
        super().__init__(command=command, parameter=parameter)
        self.file = file
        self.mode = mode
        self.ccn = ccn
        self.ce = ce
        self.cm = cm
        self.arg = arg
        self.arg2 = arg2
        self.arg3 = arg3
        self.resp = 0
        self.os = os.name

    def get_file(self):
        return self.file

    def get_mode(self):
        return self.mode

    def get_ccn(self):
        return self.ccn

    def get_ce(self):
        return self.ce

    def get_cm(self):
        return self.cm

    def get_arg(self):
        return self.arg

    def get_arg2(self):
        return self.arg2

    def get_arg3(self):
        return self.arg3

    # write a sentence (self.arg2) at a specific line(self.arg2) in a file (self.file)
    def writting(self, this):
        if self.parameter == "Y":
            with open(this, "r+") as file:
                lines = file.readlines()
                file.close()

            lines.insert(int(self.arg), self.arg2)
            with open(this, "w+") as file:
                file.writelines(lines)
                file.close()
        else:
            with open(self.file, "r+") as file:
                lines = file.readlines()
                file.close()

            lines.insert(int(self.arg), self.arg2)
            with open(self.file, "w+") as file:
                file.writelines(lines)
                file.close()

    # rewrite the content of a file ( self.arg2) at a specific line (self.arg) on a file (self.file)
    def writte_from_file(self, this, this2):
        lines2 = []
        if self.parameter == "Y":
            with open(this, "r+") as file:
                lines = file.readlines()
                file.close()

            with open(this2, "r+") as file:
                lines1 = file.readlines()
            for element in lines1:
                lines2.insert(0, element)
            for element2 in lines2:
                lines.insert(int(self.arg), element2)

            with open(this, "w+") as file:
                file.writelines(lines)
                file.close()
        else:
            with open(self.file, "r+") as file:
                lines = file.readlines()
                file.close()

            with open(self.arg2, "r+") as file:
                lines1 = file.readlines()
            for element in lines1:
                lines2.insert(0, element)
            for element2 in lines2:
                lines.insert(int(self.arg), element2)

            with open(self.file, "w+") as file:
                file.writelines(lines)
                file.close()

    # complete a file (self.arg) with the content of an other (self.file )
    # self.arg must contain "{}" indicators for know where put every line of self.file
    def write_3_file(self, this, this2):
        w = []
        fif = []
        if self.parameter == "Y":
            with open(this, "r+") as file:
                f1 = file.readlines()
                file.close()
            for element in f1:
                timelapse = element.split("\n")
                w.append(timelapse[0])
            with open(this2, "r+") as file:
                f2 = file.readlines()
                file.close()
            mix = len(w) - 1
            for x in range(0, mix):
                instant1 = w[x]
                instant2 = f2[x]
                try:
                    t = instant2.format(instant1)
                except:
                    print("Only one indicator for one line !")
                fif.append(t)
            with open(this2, "w+") as file:
                for element in fif:
                    file.write(element)
                file.close()
        else:
            with open(self.file, "r+") as file:
                f1 = file.readlines()
                file.close()
            for element in f1:
                timelapse = element.split("\n")
                w.append(timelapse[0])
            with open(self.arg, "r+") as file:
                f2 = file.readlines()
                file.close()
            mix = len(w)
            for x in range(0, mix):
                instant1 = w[x]
                instant2 = f2[x]
                try:
                    t = instant2.format(instant1)
                except:
                    print("only one indicator for one line !")
                fif.append(t)
            with open(self.arg, "w+") as file:
                for element in fif:
                    file.write(element)
                file.close()

    # execute a file (self.file)
    def execute(self, this):
        if self.parameter == "Y":
            if self.os == "posix":
                os.system("chmod +x {}".format(this))
                os.system("./{}".format(this))
            elif self.os == "nt":
                os.system("start {}".format(this))
        else:
            if self.os == "posix":
                os.system("chmod +x {}".format(self.file))
                os.system("./{}".format(self.file))
            elif self.os == "nt":
                os.system("start {}".format(self.file))

    # open a file (self.file) in his defolt app
    def openning(self, this):
        if self.parameter == "Y":
            if self.os == "posix":
                os.system("xdg-open {}".format(this))
            elif self.os == "nt":
                os.system("start {}".format(this))
        else:
            if self.os == "posix":
                os.system("xdg-open {}".format(self.file))
            elif self.os == "nt":
                os.system("start {}".format(self.file))

    # open a file (self.file) in a specific editor (self.arg)
    def open_editor(self, this):
        if self.parameter == "Y":
            if self.os == "posix":
                os.system("{} {}".format(self.arg, this))
            elif self.os == "nt":
                print("option don't exist on windows :(")
        else:
            if self.os == "posix":
                os.system("{} {}".format(self.arg, self.file))
            elif self.os == "nt":
                print("option don't exist on windows :(")

    # know which of these action do
    def mod_file(self, this, this2, this3):
        if self.mode == "e":
            self.execute(this=this)
        elif self.mode == "o":
            self.openning(this=this)
        elif self.mode == "oe":
            self.open_editor(this=this)
        elif self.mode == "w":
            self.writting(this=this)
        elif self.mode == "wf":
            self.writte_from_file(this=this, this2=this2)
        elif self.mode == "w3f":
            self.write_3_file(this=this, this2=this3)

    # cut/paste a file (self.file) in a place (self.arg3)
    def cut(self, this, this2):
        if self.parameter == "Y":
            source = this
            target = this2
        else:
            source = self.file
            target = self.arg3
        shutil.copy(source, target)
        os.remove(source)

    # copy/paste a file (self.file) in a place (self.arg3)
    def copy(self, this, this2):
        if self.parameter == "Y":
            source = this
            target = this2
        else:
            source = self.file
            target = self.arg3
        shutil.copy(source, target)

    # know what to do ( Cut / Copy / No (CCN))
    def mod_ccn(self, this, this2):
        if self.ccn == "copy":
            self.copy(this, this2)
        elif self.ccn == "cut":
            self.cut(this, this2)

    # get the content of a file
    def content_file(self, this):
        if self.parameter == "Y":
            with open(this, "r+") as file:
                r = file.readlines()
                file.close()
            c = "_".join(r)
            return c
        else:
            with open(self.file, "r+") as file:
                r = file.readlines()
                file.close()
            c = "_".join(r)
            return c

    # paste the content of a file (self.file) in entry (Content in Entry CE)
    def content_in_entry(self, entry, nb, this):
        entry.delete(0, nb)
        content = self.content_file(this=this)
        entry.insert(0, content)

    # paste a sepcific line of a file (self.file) in the entry
    def content_in_entry2(self, entry, nb, this):
        if self.parameter == "Y":
            entry.delete(0, nb)
            with open(this, "r+") as file:
                content = file.readlines()
                d = content[int(self.arg3)].split("\n")
                h = d[0]
                file.close()
            entry.insert(0, h)
            del d
            del h
        else:
            entry.delete(0, nb)
            with open(self.file, "r+") as file:
                content = file.readlines()
                d = content[int(self.arg3)].split("\n")
                h = d[0]
                file.close()
            entry.insert(0, h)
            del d
            del h

    # know what to do between content in entry , content in entry 2 and n
    def mod_ce(self, entry, nb, this):
        if self.ce == "Y":
            self.content_in_entry(entry, nb, this)
        elif self.ce == "Y2":
            self.content_in_entry2(entry, nb, this)

    # paste the content of a file (self.file) in a file named "memory.txt"
    def paste_in_memory(self, this):
        if self.parameter == "Y":
            with open(this, "r+") as file:
                lines = file.readlines()
                file.close()
        else:
            with open(self.file, "r+") as file:
                lines = file.readlines()
                file.close()
        with open("memory.txt", "a+") as file:
            for line in lines:
                file.write(line)
            file.close()

    # know what to do between content in memory and n
    def mod_cm(self, this):
        if self.cm == "Y":
            self.paste_in_memory(this)

    # all verifications in a big one ( advantage = by type one command we
    # start all verifications )
    def big_one(self, entry, nb, this, this2, this3):
        th = self.file.format(this)
        t = self.arg.format(this2)
        tt = self.arg2.format(this2)
        ttt = self.arg3.format(this3)
        self.mod_file(this=th, this2=tt, this3=t)
        self.mod_ccn(th, ttt)
        self.mod_ce(entry, nb, th)
        self.mod_cm(th)

    def filewrite(self, ee):
        with open(self.file, "a+") as file:
            for x in ee:
                file.write(x + "\n")
            file.close()


class Ccmd(Dothis):
    # this object will type one or more command in terminal when type command name associate
    def __init__(self, command, exe, parameter):
        super().__init__(command=command, parameter=parameter)
        self.exe = exe

    def get_exe(self):
        return self.exe

    def todo(self, this):
        h = self.exe.split(".....")
        if self.parameter == "Y":
            for element in h:
                tod = this
                todo = element.format(tod)
                os.system(todo)
        else:
            for element in h:
                os.system(element)
