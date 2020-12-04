import json
import re
from dataclasses import dataclass


def validate_range(year: int, min: int, max: int):
    if not min <= year <= max:
        raise ValueError(f'{year} outside range {min}-{max}')
    return year


def validate_height(h: str):
    if h.endswith("in") and 59 <= int(h.split("in")[0]) <= 76:
        return h
    if h.endswith("cm") and 150 <= int(h.split("cm")[0]) <= 193:
        return h
    raise ValueError(f'Invalid height: {h}')


def validate_hair_color(hcl):
    if re.search("^#[0-9a-f]{6}$", hcl) is None:
        raise ValueError(f'Invalid hair color: {hcl}')
    return hcl


def validate_eye_color(clr: str):
    if re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", clr) is None:
        raise ValueError(f'Invalid eye color: {clr}')
    return clr


def validate_passport_id(pid: str):
    if re.search("^[0-9]{9}$", pid) is None:
        raise ValueError


@dataclass
class Passport:
    birth_year: int
    issue_year: int
    expiration_year: int
    height: str
    hair_color: str
    eye_color: str
    passport_id: str

    def __init__(self, j):
        d = json.loads(j)
        self.birth_year = validate_range(int(d['byr']), 1920, 2002)
        self.issue_year = validate_range(int(d['iyr']), 2010, 2020)
        self.expiration_year = validate_range(int(d['eyr']), 2020, 2030)
        self.height = validate_height(d['hgt'])
        self.hair_color = validate_hair_color(d['hcl'])
        self.eye_color = validate_eye_color(d['ecl'])
        self.passport_id = validate_passport_id(d['pid'])


def transform_to_json(passport_txt):
    json_passport = "{" + re.sub("([a-z]{3}):([a-z0-9#]+)", r'"\1": "\2",', passport_txt.replace(r"\n", " ")) + "}"
    return json_passport.replace(",}", "}")


def split_passports(s):
    return re.split(r"\n\n", s)


def try_parse_passport(s):
    try:
        return Passport(s)
    except:
        # print(traceback.format_exc())
        return None


raw = open("../inputs/day4.txt").read()
json_passports = [transform_to_json(passport) for passport in split_passports(raw)]

print(sum(1 for passport in [try_parse_passport(s) for s in json_passports] if passport is not None))
