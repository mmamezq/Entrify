from firebase_admin import initialize_app, credentials, firestore

cred = credentials.Certificate('nlpproject-395000-66ebd7aa5702.json')
initialize_app(cred)
db = firestore.client()

def create_job(job_item):
    doc_ref = db.collection("jobs").document(job_item["job_id"])
    doc_ref.set(job_item)
    print(job_item["job_id"], "created in db.")