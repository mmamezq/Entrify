import random
from model import db, Job


def get_job(id):
    return Job.query.filter(Job.job_id == id).first()


def get_all_ids():
    id_list = [x[0] for x in Job.query.with_entities(Job.job_id).all()]
    random.shuffle(id_list)
    return id_list


def get_unlabelled_job_ids():
    id_list = [x[0] for x in Job.query.filter(Job.label == -1, (Job.uncertain == 0) | (Job.uncertain == None)).with_entities(Job.job_id).all()]
    random.shuffle(id_list)
    return id_list


def get_uncertain_job_ids():
    id_list = [x[0] for x in Job.query.filter(Job.uncertain == 1).with_entities(Job.job_id).all()]
    random.shuffle(id_list)
    return id_list


def get_entry_job_ids():
    id_list = [x[0] for x in Job.query.filter(Job.label == 1, (Job.uncertain == 0) | (Job.uncertain == None)).with_entities(Job.job_id).all()]
    random.shuffle(id_list)
    return id_list


def get_advanced_job_ids():
    id_list = [x[0] for x in Job.query.filter(Job.label == 0, (Job.uncertain == 0) | (Job.uncertain == None)).with_entities(Job.job_id).all()]
    random.shuffle(id_list)
    return id_list


def get_labelled_count():
    return Job.query.filter(Job.label != -1).count()


def update_uncertainty(obj, uncertain):
    obj.uncertain = uncertain
    db.session.commit()


def update_job_label(id, label):
    obj = get_job(id)

    if label == 'None':
        update_uncertainty(obj, 1)
        return
    
    update_uncertainty(obj, 0)
    obj.label = label

    db.session.commit()