# AlphaDHE - DiffieHellman Ephemeral for A-Z ciphers
Note: Requires MASHHASH and pycrypto to be installed.

Uses 1024 bit primes by default.  The alpha.py script allows two parties to develop a shared secret by exchanging values.  The resulting secret key is hashed using MASH to create a key of desired size. (Default is 16 letters, maximum is 32)

# Script usage:

Initiator: python alpha.py init  
Other party: python alpha.py  

# Example  

- Initiator generates g, p and his secret  

Initial step: Send g and p to your peer  
g: BFHJJCAGACDCJDDFCIJHIFIFJJFFEBEBECEJDIGHDADCIIEDIBDJDEBEDAFGAEHDIEFJJFHDGADEGEABAHFGBHGBFCBFABFJHFHFJHIEBDFJDCJCJBBEDJFCIJHHDCJHABBJBGGGFJHGDJEJBHJFEFCAECAAEHIFIIEGHJBBBGIFJFBGBDJIHJCFEAGBDBBDBFHIAJBAHICIGEFFJIAIGGHADGCFFGEIEBGBFCGFBFGGIJBCACDIJBAJFADEEADIBAHHGDFHDJCJJAJFACHBGJIFGIFIHAGJECBHIBHIDHEHHJECIDEAD  
p: BAJHHDBAIFHIFJDCCGCFDFEJGJJHFDBJEGEJCDBBFBIHJADHGHDHDCCHACBJHCGGDBIABHBIEHJHGHAJIIJCEGGJEFHIDJDDHBICIEEBJEEJGCBAHBBCECJEEBGGGGHJBJAJIAAGEEBDEDAGFECHHBICJBCIEFEDDBGJICGHHDEEIHAAADFAHIFCIJJCEEDGEBIGBCCECHBEFEGHGIEFJEBABDACBIFFGBBGBGIHJEIHGJBAEJAEHCIBFDCIGDJDIBGCBBJIIBHCIDIBHHGABDBGJHEJEFEEJAGDEHBBFAEEAIDAIHCJJ  
Step 1: Send this to your peer  
DDJICJJFHHAIHFGBHEJIBEHAJHEBEFCIAIJECDIDBHFEBIHBFFJBAGGHJBAIAACBJDJBDEDFAACGGFACHIJGAFJJDAFJDAJFHAFJGEIGIJJDBBHHAEGDDGAFEFDDDBJFJGIACBHBCCAAAAIECAEGAHGJFGGADBCDEJGBGAIGFHDIDCDIFJCCJJFCDEAIDJEBAHHAGBBJHFDEJICEJCDEGFGEHCHGCBHCCHBGEEEHBBAHEGGDIGECDHGDCEHDABJABCBIBGDBHCFAIICDHCGJGAAFBEJIDECEHACGAJDAEBDJBBAFAJC  

- Other party generates a secret and inputs the inititor's g and p values and calculates step1 which is sent to the initiator.  

Enter your peer's g value: BFHJJCAGACDCJDDFCIJHIFIFJJFFEBEBECEJDIGHDADCIIEDIBDJDEBEDAFGAEHDIEFJJFHDGADEGEABAHFGBHGBFCBFABFJHFHFJHIEBDFJDCJCJBBEDJFCIJHHDCJHABBJBGGGFJHGDJEJBHJFEFCAECAAEHIFIIEGHJBBBGIFJFBGBDJIHJCFEAGBDBBDBFHIAJBAHICIGEFFJIAIGGHADGCFFGEIEBGBFCGFBFGGIJBCACDIJBAJFADEEADIBAHHGDFHDJCJJAJFACHBGJIFGIFIHAGJECBHIBHIDHEHHJECIDEAD  
Enter your peer's p value: BAJHHDBAIFHIFJDCCGCFDFEJGJJHFDBJEGEJCDBBFBIHJADHGHDHDCCHACBJHCGGDBIABHBIEHJHGHAJIIJCEGGJEFHIDJDDHBICIEEBJEEJGCBAHBBCECJEEBGGGGHJBJAJIAAGEEBDEDAGFECHHBICJBCIEFEDDBGJICGHHDEEIHAAADFAHIFCIJJCEEDGEBIGBCCECHBEFEGHGIEFJEBABDACBIFFGBBGBGIHJEIHGJBAEJAEHCIBFDCIGDJDIBGCBBJIIBHCIDIBHHGABDBGJHEJEFEEJAGDEHBBFAEEAIDAIHCJJ  
Step 1: Send this to your peer  
BHIJDBJEGGBEDJJDBGECHHIAIDEDFJGEAIAGIEAHJHBJIFGHIADGJJGDDCFJCEGEJIIDEEHDJGCFHACEAHAAFIBIGIFDCDDJEBDIAJEHHHHDICEDEIJBIFBJEJDIJCFIIBGEHDDGBHGEFEGJGEBAHCGDAHECHIJEEJAHIDJHCJDFFAACDAFDDEIJDIBFJJEJDFJAJJDBJDJDGGCCEGCAIDBDCBAADEJGCAIHGEHDCGHFBDCIHBHJFAFAACEJBIADCHGDECHEEDAEEGJJHHHDCEAAACEIGEJGCEJIBFAGIFBAFDFFAAB  

 
- Initiator calculates step1, hashes the result and arrives at the secret key

Enter peer's step 1: BHIJDBJEGGBEDJJDBGECHHIAIDEDFJGEAIAGIEAHJHBJIFGHIADGJJGDDCFJCEGEJIIDEEHDJGCFHACEAHAAFIBIGIFDCDDJEBDIAJEHHHHDICEDEIJBIFBJEJDIJCFIIBGEHDDGBHGEFEGJGEBAHCGDAHECHIJEEJAHIDJHCJDFFAACDAFDDEIJDIBFJJEJDFJAJJDBJDJDGGCCEGCAIDBDCBAADEJGCAIHGEHDCGHFBDCIHBHJFAFAACEJBIADCHGDECHEEDAEEGJJHHHDCEAAACEIGEJGCEJIBFAGIFBAFDFFAAB  
Secret Session key: QYPMITUSMHCYCZEC  

- Other part calculates step1, hashes the result and arrives at the secret key  

Enter peer's step 1: DDJICJJFHHAIHFGBHEJIBEHAJHEBEFCIAIJECDIDBHFEBIHBFFJBAGGHJBAIAACBJDJBDEDFAACGGFACHIJGAFJJDAFJDAJFHAFJGEIGIJJDBBHHAEGDDGAFEFDDDBJFJGIACBHBCCAAAAIECAEGAHGJFGGADBCDEJGBGAIGFHDIDCDIFJCCJJFCDEAIDJEBAHHAGBBJHFDEJICEJCDEGFGEHCHGCBHCCHBGEEEHBBAHEGGDIGECDHGDCEHDABJABCBIBGDBHCFAIICDHCGJGAAFBEJIDECEHACGAJDAEBDJBBAFAJC  
Secret Session key: QYPMITUSMHCYCZEC  

