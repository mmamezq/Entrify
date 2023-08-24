import random
from model import db, Job


def get_all_ids():
    return [x[0] for x in Job.query.with_entities(Job.job_id).all()]


def get_unlabelled_job_ids():
    return [x[0] for x in Job.query.filter(Job.label == -1).with_entities(Job.job_id).all()]


def get_uncertain_job_ids():
    return [x[0] for x in Job.query.filter(Job.uncertain == 1).with_entities(Job.job_id).all()]


def get_entry_job_ids():
    return [x[0] for x in Job.query.filter(Job.label == 1, (Job.uncertain == 0) | (Job.uncertain == None)).with_entities(Job.job_id).all()]


def get_advanced_job_ids():
    return [x[0] for x in Job.query.filter(Job.label == 0, (Job.uncertain == 0) | (Job.uncertain == None)).with_entities(Job.job_id).all()]


def get_random_job(id_list):
    random_indx = random.choice(id_list)
    return Job.query.filter(Job.job_id == random_indx).first()