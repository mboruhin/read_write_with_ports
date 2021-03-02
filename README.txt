at ww station

------ for server ------
in host terminal:
d:
docker run -it -v ${PWD}/read_write_with_ports:/project_copy -p 4100:4100/udp full_with_requirements
inside docker:
cd project_copy
python3 server-c.py

------ for client ------
in host terminal:
d:
docker run -it -v ${PWD}/read_write_with_ports:/project_copy full_with_requirements
inside docker:
cd project_copy
python3 client-c.py