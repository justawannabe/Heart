import os


class Patient_class_rec:
    def __init__(self,
        age,
        sex,
        cp,
        trestbps
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal,
        target,
        id):
        self.age = age
        self.sex = sex
        self.cp  = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs  = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang   = exang
        self.oldpeak = oldpeak
        self.slope   = slope
        self.ca      = ca
        self.thal    = thal
        self.target  = target
        self.id      = id


heart_data_path = "C:/Users/noeld/VSCode-Python/Heart/data/heart-uid.csv"
path_out = "C:/Users/noeld/VSCode-Python/Heart/data/heart-out.csv"


def load_patient_data(path):
    patients_dict = {}                            # change to dict {} was a list []
    with open(path, 'r') as file_in:
        for i, row in enumerate(file_in):
            if i == 0:                            # Skip over first row as it is a header
                file_out = open(path_out, 'w')    # open output file as part of first row skip over
                continue   
             
            row_out = row
            row = row.strip()     # strip eol
            row = row.split(',')  # convert from csv comma format into list w comma delim
            patient_data = [float(num_in) for num_in in row[:-1]] # convert input numbers to float - last field [-1] is str ID 
            patient_data.append(row[-1])                    # pt id is str, no float chg, add id at end of patient_data
            #patients[patient_data[-1]] = patient_data       # pt id set equal to patient data {pt_id, paitent_data} - dict
            ## {'1': [63.0, 1.0, 3.0, 145.0, 233.0, 1.0, 0.0, 150.0, 0.0, 2.3, 0.0, 0.0, 1.0, 1.0, '1'],
            ##  '2': [37.0, 1.0, 2.0, 130.0, 250.0, 0.0, 1.0, 187.0, 0.0, 3.5, 0.0, 0.0, 2.0, 1.0, '2']
            #   print('\n', patient_data)
            ##  
            patient = Patient_class_rec(*patient_data)          # Patient class takes in patient data and assigns names
                                                                # note "*patient_data" i/p consists of many fields
            patients_dict[patient.id]  =  patient          # using a dict assign patient ID to it's data record for lookup
            file_out.write(row_out)                   # I added output file 
    file_out.close()
    print(i)
    # print(patients_dict)
    return(patients_dict)


def find_patient(patients, uid):
    return patients[uid]


def get_patient_attr(patient, attr, comp=None):        # patients is one row of patient data
    if hasattr(patient, attr):
        return getattr(patient, attr)           # "getattr" - built-in function
    elif comp:
        return comp.compute(patient, attr)
    else:
        raise AttributeError

class BaseCompute:
    def compute(self, patient, attr):
        fn = getattr(self, attr)
        result = fn(patient)
        return result

        
class PatientsCompute(BaseCompute):
    def __init__(self, patients):
        self.patients = patients

    def chol_percentile(self, patient):
        return "80th"


patients = load_patient_data(heart_data_path)
print("addr of 'patients': ", id(patients))
## print(patients)       # {'1': <__main__.Patient_class_rec object at 0x000001E248A74A60>, '2': <__main_
p = find_patient(patients, '231')         # patients is returned from "get_patient_data"
# chol = get_patient_attr(p, "chol")        # cholesterol is 5th element, 0 is the first
comp = PatientsCompute(patients)
percentile = get_patient_attr(p, "chol_percentile", comp)
print(" print(p) output: ", p)                                  # <__main__.Patient_class_rec object at 0x00000264682357C0>
print("addr of 'p': ", id(p))
print(p)
print(percentile)