from pwn import * # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])

to_send = {
    "buy": "flag"
}
json_send(to_send)

json_recv()


# 6d616b696e675f6c7578656d626f7572675f6469736170706f696e746564 making_luxembourg_disappointed
# dmVyaWZpY2F0aW9uX3NlcGFyYXRlZF9hcHBlYWw= verification_separated_appeal
# Z2l2ZV9jb3VwbGVkX2JyaWNr give_coupled_brick
# 746563686e6f6c6f67795f636875636b5f696e6e6f766174697665 technology_chuck_innovative
#creatures_song_both
#really_essex_intake
#adelaide_transactions_calls
#password_struck_finished
#lincoln_fighting_teachers
#ukraine_hearings_transparenc
#authorization_inspired_chairs
#regardless_delays_feedback
#fvtug_ob_enprf
#