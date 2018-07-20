--------------------------------
-- AI
--------------------------------
NDefines.NAI.AGGRESSIVENESS = 2000 -- Base chance (out of 10000) of AI being willing to start a war each diplomatic tick (~1.5 times a month)
NDefines.NAI.AGGRESSIVENESS_BONUS_EASY_WAR = 1500 -- Added to aggressiveness if the war is against a weak or particularily hated enemy

NDefines.NAI.PEACE_WAR_DIRECTION_WINNING_MULT = 100.0 -- Multiplies AI emphasis on war direction if it's the one making gains
NDefines.NAI.PEACE_FORCE_BALANCE_FACTOR = 0.01 -- AI willingness to peace based on strength estimation of both sides
NDefines.NAI.PEACE_MILITARY_STRENGTH_FACTOR = 50 -- AI unwillingness to peace based on manpower & forcelimits
NDefines.NAI.PEACE_WARGOAL_FACTOR = 1 -- AI unwillingness to peace based on holding the wargoal
NDefines.NAI.PEACE_CALL_FOR_PEACE_FACTOR = 1	-- How much AI wants peace based on having call for peace

NDefines.NAI.DIPLOMATIC_INTEREST_DISTANCE = 1500 -- If border distance is greater than this, diplomatic AI will have less interest in the country
NDefines.NAI.CONQUEST_INTEREST_DISTANCE = 1000 -- Beyond this range, AI is less interested in conquest of provinces
