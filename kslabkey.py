import labkey

def getList(reqData, *args):
    projName = args[0]
    schemaType = args[1]
    targetName = args[2]
    filters = []

    # process filters
    for k in reqData.keys():
        filters.append([ k, 'eq', reqData[k]])

    kinomeTable = labkey.query.selectRows(
        baseUrl = 'http://localhost:8080/labkey',
        containerPath = projName,
        schemaName = schemaType,
        queryName = targetName,
        filterArray = filters
    )
    
    #return rowMatch
    import pdb; pdb.set_trace()
    return kinomeTable

