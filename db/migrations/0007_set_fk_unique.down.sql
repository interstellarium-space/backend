ALTER TABLE IF EXISTS designers
    DROP CONSTRAINT IF EXISTS designer_user_unique;
ALTER TABLE IF EXISTS engineers
    DROP CONSTRAINT IF EXISTS engineer_user_unique;
ALTER TABLE IF EXISTS technicians
    DROP CONSTRAINT IF EXISTS technician_user_unique;
ALTER TABLE IF EXISTS laboratorians
    DROP CONSTRAINT IF EXISTS laboratorian_user_unique;
ALTER TABLE IF EXISTS departments
    DROP CONSTRAINT IF EXISTS department_leader_unique;
