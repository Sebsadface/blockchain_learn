// SPDX-License-Identifier: MIT 
pragma solidity >=0.6.5;

contract SeaCliff {
    event UpdatedMessages(string oldStr, string newStr);

    string public message;

    constructor(string memory initmessage) public {
        message = initmessage;
    }

    function update(string memory newMessage) public {
        string memory oldMsg = message;
        message = newMessage;
        emit UpdatedMessages(oldMsg, newMessage);
    }
}
